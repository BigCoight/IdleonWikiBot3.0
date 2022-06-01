import difflib
import os

import jsbeautifier
import regex as re
from regex import Pattern


class CodeSplitter:
	@classmethod
	def Split(cls, parsedFile: str, version: str) -> None:
		chunkFinder: Pattern = re.compile(
			r"\((.+?\.(\w*) = function (\([^)(]*+(?:(?3)[^)(]*)*+\)) (\{[^}{]*+(?:(?4)[^}{]*)*+\}))")
		chunks = re.findall(chunkFinder, parsedFile)
		opts = jsbeautifier.default_options()
		opts.indent_size = 4
		opts.space_in_empty_paren = False
		opts.brace_style = "collapse"
		opts.indent_with_tabs = True
		opts.preserve_newlines = False
		opts.break_chained_methods = True

		for chunk in chunks:
			try:
				pretty_chunk = jsbeautifier.beautify(chunk[0], opts)
			except AttributeError:
				print(chunk[1])
				continue
			with open(cls._getPath(version, chunk[1]), mode = "w") as outfile:

				outfile.write(pretty_chunk)

	@classmethod
	def _getPath(cls, version: str, name: str) -> str:
		path = fr"./codefiles/codechunks/{version}/"
		if not os.path.isdir(path):
			os.makedirs(path, exist_ok = True)

		return path + f"{name}.txt"

	@classmethod
	def tokenise(cls):
		def onlyDelta(x: str) -> bool:
			return x.startswith("+") or x.startswith("-")

		with open(r"./codefiles/codechunks/157/_customBlock_RunCodeOfTypeXforThingY.txt", mode = "r") as infile:
			lines1 = infile.read()
		with open(r"./codefiles/codechunks/158/_customBlock_RunCodeOfTypeXforThingY.txt", mode = "r") as infile:
			lines2 = infile.read()
		print("\n".join([x for x in difflib.unified_diff(lines1.splitlines(), lines2.splitlines())]))

	# print([token.string for token in toks1])
	# print([token.string for token in toks2])
	# print([tok_name[token.exact_type] for token in toks1])
	# print([tok_name[token.exact_type] for token in toks2])
	# print("---EOL---")

	@classmethod
	def parseTypeChecks(cls, chunk: str) -> str:
		biglist = r"var bigList = {[\w\s\d:\?'=.\(\),&|$\n\/:;+-{}]+?},"
		removeNulls = r"\w = null != .*? (.\.getReserved\(\"(.*?)\"\)) : .*?\2"
		removeSetNullChecks = r"null != .*? (.\.setReserved\(\"(.*?)\", (.*?)\)) : .*?\2 = \3\)"
		pattern00 = r"null == ([\$\w]+)? \? 0[\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)"
		pattern10 = r"null == ([\$\w]+)? \|\| [\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)\)"
		pattern11 = r"null == \(([\$\w]+)([\w\s\d\n:_?\'\"=.\(\),&|$]+?)\) \? 0[\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)"
		pattern2 = r"null == ([\$\w]+) = (([[\]\w\s\d\n\'\"?|!-=])+?) \? 0[\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)"
		pattern20 = r"null == \(([\$\w]+) = (([[\]\w\s\d\n\'\"?|!-=])+?)\) (\?|\|) (0|\|) [\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)(,|;)?"
		pattern21 = r"null == \(([\$\w]+) = (([[\]\w\s\d\n\'\"?|!-=])+?) \? 0[\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)\)"
		pattern3 = r"\(null == \(([\$\w]+) = (([[\]\w\s\d\n\'\"?|!-=])+?)\) \|\| [\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)\)(,|;)?"
		pattern31 = r"null == \(([\$\w]+) = (([[\]\w\s\d\n\'\"?|!-=])+?)\) \|\| [\w\s\d\n:_?\'\"=.\(\),&|$]+?\1\)\)\)(,|;)?"
		reparse = r"parsenum_([\$\w]+)?"
		parsenum = "\nfunction parseNum(num) {\n  let cast = function (a, b) {\n    if (null == a || a instanceof b) return a;\n    throw new Error('Cannot cast ' + String(a) + ' to ' + String(b));\n  }\n  return null == num ? 0\n    : 'number' == typeof num ? cast(num, Number)\n      : 'number' == typeof num && (num | 0) === num ? cast(num, {}) :\n        'boolean' == typeof num ? cast(num, Boolean) ? 1 : 0\n          : 'string' == typeof num ? parseFloat(num) : parseFloat(f.string(num))\n}"
		listbig = re.compile(biglist)

		conv00 = re.compile(pattern00)
		conv10 = re.compile(pattern10)
		conv11 = re.compile(pattern11)
		conv2 = re.compile(pattern2)
		conv20 = re.compile(pattern20)
		conv21 = re.compile(pattern21)
		conv3 = re.compile(pattern3)
		conv31 = re.compile(pattern31)
		rep = re.compile(reparse)

		nfile, b = listbig.subn(r"", chunk)

		nfile, n00 = conv00.subn(r"parsenum_\1", nfile)
		nfile, n10 = conv10.subn(r"parsenum_\1", nfile)
		nfile, n11 = conv11.subn(r"parsenum_\1\2", nfile)
		nfile, n2 = conv2.subn(r"parsenum_\1 = \3", nfile)
		nfile, n20 = conv20.subn(r"parsenum_\1 = \2\6", nfile)
		nfile, n3 = conv3.subn(r"parsenum_\1 = \2\4", nfile)
		nfile, n21 = conv21.subn(r"parsenum_\1 = \2", nfile)
		nfile, n22 = conv20.subn(r"parsenum_\1 = \2\6", nfile)
		nfile, n31 = conv31.subn(r"parsenum_\1 = \2\4", nfile)
		nfile, Fi = rep.subn(r"parsenum(\1)", nfile)
		return nfile
