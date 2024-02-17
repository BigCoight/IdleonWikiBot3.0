import re
from typing import List

from definitions.component.ComponentFactory import ComponentFactory
from definitions.misc.world2.Bubble import Bubble, Cauldron
from helpers.HelperFunctions import replaceUnderscores, reAll
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class BubbleRepo(Repository[Cauldron]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

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
		reEverything = fr'"({reAll}*)"\.'
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
						bubbleReq.append(ComponentFactory.getComponent(bubData[i], bubData[j]))
						continue
					bubbleReq.append(ComponentFactory.getComponent(bubData[i], -1))

				toAdd = Bubble(
					cauldron = bubbleNames[n],
					name = bubData[0],
					x1 = bubData[1],
					x2 = bubData[2],
					func = bubData[3],
					description = bubData[9],
					requirements = bubbleReq.copy(),
					bonusKey = bubData[-1]
				)

				cls.addToCauldron(bubbleNames[n], toAdd)

	@classmethod
	def addToCauldron(cls, cauldron: str, bubble: Bubble):
		if not cls.contains(cauldron):
			cls.add(cauldron, Cauldron(bubbles = []))
		cls.get(cauldron).bubbles.append(bubble)
