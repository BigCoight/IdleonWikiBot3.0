import re
from typing import List

from definitions.common.LiquidComponent import LiquidComponent
from definitions.misc.world2.Bubble import Bubble
from definitions.common.Component import Component
from helpers.HelperFunctions import replaceUnderscores, camelCaseToTitle
from repositories.master.Repository import Repository


class BubbleRepo(Repository[Bubble]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def parse(cls, value) -> Bubble:
		return Bubble.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Bubbles"]

	@classmethod
	def generateRepo(cls) -> None:
		bubbleNames = ["Power Cauldron", "Quicc Cauldron", "High-IQ Cauldron", "Kazam Cauldron", "Vials",
		               "Liquid Shop", "??"]
		bubbleData = cls.getSection().split("],")
		reEverything = r'"([a-zA-Z0-9_ +{}\',.\-%!$:`?;\n\]\(\)]*)"\.'
		for n, v in enumerate(bubbleData):
			bubbles = re.findall(reEverything, v)
			for bubble in bubbles:
				bubData = bubble.split(" ")
				bubData[0] = replaceUnderscores(bubData[0]).title()
				if bubData[-1] == "Filler":
					continue
				if len(bubData) < 9:
					continue
				bubbleReq = []
				for i, j in zip([5, 6, 7, 8], [11, 12, 13, 14]):
					if bubData[i] == "Blank":
						break
					if len(bubData) > 14:
						if bubData[i][:6] == "Liquid":
							bubbleReq.append(LiquidComponent(liquidNo = bubData[i][6], quantity = bubData[j]))
							continue
						bubbleReq.append(Component(item = bubData[i], quantity = bubData[j]))
						continue
					if bubData[i][:6] == "Liquid":
						bubbleReq.append(LiquidComponent(liquidNo = bubData[i][6], quantity = -1))
						continue
					bubbleReq.append(Component(item = bubData[i], quantity = -1))
				cls.add(bubData[0], Bubble(
					cauldron = bubbleNames[n],
					x1 = bubData[1],
					x2 = bubData[2],
					func = bubData[3],
					description = bubData[9],
					requirements = bubbleReq.copy()
				))

	@classmethod
	def _writeChangesWiki(cls, differences):
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + f"{v}|0" + "}}\n"

		res = ""
		new = differences["new"]
		changes = differences["changes"]

		changesOrdered = {}
		for key in changes.keys():
			cType = cls.get(key).cauldron
			if cType not in changesOrdered:
				changesOrdered[cType] = []
			changesOrdered[cType].append(key)

		newOrdered = {}
		for key in new.keys():
			cType = cls.get(key).cauldron
			if cType not in newOrdered:
				newOrdered[cType] = []
			newOrdered[cType].append(key)
		res += "<div class=\"GenericFlex\"><div class=\"GenericChild\">\n"
		res += "==Changes==\n"
		for typ, keys in changesOrdered.items():
			res += head(typ)
			for change in keys:
				res += bold(cls.getWikiName(change))
				res += cls._writeChangelog(changes[change], 1)
			res += "|}\n\n"

		res += "</div><div class=\"GenericChild\">\n"
		res += "==New==\n"
		for typ, keys in newOrdered.items():
			res += head(typ)
			for change in keys:
				res += bold(cls.getWikiName(change))
				res += cls._writeChangelog(new[change], 1)
			res += "|}\n\n"

		res += "</div></div>"

		with open(cls._getPath("wikitext/_changes", "txt"), mode = 'w') as infile:
			infile.write(res)
