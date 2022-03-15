import os
import threading
from multiprocessing.dummy import Pool
from tokenize import generate_tokens

import regex as re
from re import Match
from difflib import SequenceMatcher
from pathlib import Path


class ReParser:
	reVarUsedInNextLine = re.compile(r'\s*\(?(?:var )?(?<!\w)([^()\s]+) = (.*)?(?<!\+\+)[;, ]\n(.*)(?<=[^a-zA-Z])(\1)(?=[^a-zA-Z])(.*)')
	reVarUsedInSameLine = re.compile(r'(?<!for \(var )\(?(?<= )([^()\s]+) = (.*?)?[;, ](.*)(?<![\w])(\1)(?=[^a-zA-Z])(.*)')

	reRemoveVar = re.compile(r'var ')
	reOneLineEqn = re.compile(r'([+\-\*\/])\n\s*')
	reOneLineExpr = re.compile(r'([,(])\n\s*')
	reOneLineBr = re.compile(r'([(])\n\s*')
	reOneLine = re.compile(r'(\S+ =)\n\s*')

	reBinOr = re.compile(r'0 \| (\w*)')
	reBinOr2 = re.compile(r'(?<=\[)(.*) \| 0(?=\])')
	reCast = re.compile(r'\w+.__cast\((.*), .*?\)')

	reGetGameAttribute = re.compile(r'[\S]\.engine\.getGameAttribute\("([\S]*)"\)')
	reSetGameAttribute = re.compile(r'[\S]\.engine\.gameAttributes\.set\("([\S]*)", (.*)\)')
	reStringCasting = re.compile(r'"" \+ \S\.string\((.*?)\)')
	reNullChecksBrackets = re.compile(r'\(null != .*? \? (.*?) : .*?\)')
	reNullChecksSingle = re.compile(r'null != .*? \? (.*?) : [\w.]*(?:\((?>[^()]+|(?1))*\))?')
	reGetReserved = re.compile(r'getReserved')
	reSetReserved = re.compile(r'setReserved')
	reCustomBlock = re.compile(r'\S\._customBlock')
	reAssignMath = re.compile(r'( *)(.*) = (?:parsenum\()?(\2)\)? ([+\-*\/]) (.*);')

	reParseNumBlank = re.compile(r'parsenum\(\w\) = ')

	reDetectRepeated = re.compile(r'([^\s(){}]*)(\((?>[^()]+|(?2))*\))')

	reVarInput = re.compile(r'((?<=[ [])[a-zA-Z]{1,2}(?!\w|\.)|[a-zA-Z]{1,2}(?= ))')


def debug(match: Match):
	print(match[1])
	return f'\n{match[3]}{match[2]}{match[5]}'


class Parser:
	def __init__(self, oldFileName):
		with open(f"{oldFileName}", "r") as inFile:
			self.text = inFile.read()

	def tryDetectRepeatedCode(self):

		brackets = ReParser.reDetectRepeated.findall(self.text)
		toCheckAgain = [x[1][1:-1] for x in brackets if x[1][0] == "("]
		codeBlocks = ["".join(x) for x in brackets]

		while len(toCheckAgain) > 1:
			newTexts = toCheckAgain.copy()
			toCheckAgain = []
			for newText in newTexts:
				newMatches = ReParser.reDetectRepeated.findall(newText)
				codeBlocks.extend(["".join(x) for x in newMatches])
				toCheckAgain.extend([x[1][1:-1] for x in newMatches if x[1][0] == "("])

		goodCodeBlocks = []
		for x in codeBlocks:
			if '=' in x: continue
			if 'parsenum' == x[0:8]: continue
			goodCodeBlocks.append(x)


		dupeBlocks = list_duplicates(goodCodeBlocks)
		print(dupeBlocks)
		restBlocks = [x for x in codeBlocks if x not in dupeBlocks]

		#self.tryMakeFunctions(restBlocks)

		dupeBlocks = [x for x in dupeBlocks if len(x) > 2 and x[0] not in ['.', "[","]"] or len(x) > 15]
		varAssignment = {}

		for i, block in enumerate(dupeBlocks):
			blockVars = ReParser.reVarInput.findall(block)
			if not blockVars:
				varAssignment[f"temp{i}"] = block
				continue
			varsOut = ", ".join(list(set(blockVars)))
			varAssignment[f"fn{i}({varsOut})"] = block

		header = ""
		for name, block in varAssignment.items():
			self.text = self.text.replace(block, name)

			header += f"var {name} = {block};\n"

		self.text = header + self.text

	def tryMakeFunctions(self, restBlocks):
		similarBlocks = set()
		for block1 in reversed(restBlocks):
			for block2 in reversed(restBlocks):
				if block1 == block2: continue
				ratio = SequenceMatcher(None, block1, block2).ratio()
				if ratio <= 0.95: continue
				similarBlocks.add(block1)

		listSimilarBlocks = list(similarBlocks)
		a = listSimilarBlocks[0]
		b = listSimilarBlocks[1]

		print(a)
		print(b)
		startMix = -1
		endMix = -1
		for i in range(len(a)):
			if a[i] != b[i]:
				if startMix == -1:
					startMix = i
			else:
				if startMix != -1:
					endMix = i
					break

		capturedVars = [x[startMix:endMix] for x in listSimilarBlocks]
		print(capturedVars)

	def Parse(self, outPath):
		# Just formatting
		self.text = ReParser.reBinOr.sub(r"\1", self.text)
		self.text = ReParser.reBinOr2.sub(r"\1", self.text)
		self.text = ReParser.reGetGameAttribute.sub(r'\1', self.text)
		self.text = ReParser.reSetGameAttribute.sub(r'\1 = \2', self.text)
		self.text = ReParser.reStringCasting.sub(r'string(\1)', self.text)
		self.text = ReParser.reGetReserved.sub('get', self.text)
		self.text = ReParser.reSetReserved.sub('set', self.text)
		self.text = ReParser.reCustomBlock.sub("cb", self.text)

		self.text = ReParser.reNullChecksSingle.sub(r'\1', self.text)
		self.text = ReParser.reCast.sub(r"\1", self.text)

		self.text = ReParser.reOneLineEqn.sub(r"\1 ", self.text)
		self.text = ReParser.reOneLine.sub(r"\1 ", self.text)
		self.text = ReParser.reOneLineBr.sub(r"\1", self.text)
		for i in range(10):
			self.text = ReParser.reVarUsedInNextLine.sub(r"\n\3\2\5", self.text)
			self.text = ReParser.reVarUsedInSameLine.sub(r"\3\2\5", self.text)

		#self.text = ReParser.reOneLineExpr.sub(r"\1 ", self.text)
		self.text = ReParser.reAssignMath.sub(r"\1\2 \4= \5;", self.text)
		self.text = ReParser.reParseNumBlank.sub("", self.text)

		for i in range(3):
			self.text = ReParser.reVarUsedInSameLine.sub(r"\3\2\5", self.text)

		#self.tryDetectRepeatedCode()

		with open(f"{outPath}", "w") as outfile:
			outfile.write(self.text)


def list_duplicates(seq):
	seen = set()
	seen_add = seen.add
	# adds all elements it doesn't know yet to seen and all other to seen_twice
	seen_twice = set(x for x in seq if x in seen or seen_add(x))
	# turn the set into a list (as requested)
	return list(seen_twice)


def parse_single_file():
	parser = Parser("./textParsing.txt")
	parser.Parse("./textParsingParsed.txt")

	# import token
	# with open("./textParsing.txt", "r") as infile:
	# 	print([token.tok_name[x.exact_type] for x in generate_tokens(infile.read)])



if __name__ == "__main__":
	parse_single_file()
