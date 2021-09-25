from typing import List

from definitions.RefineryCost import RefineryCost
from definitions.common.Component import Component
from helpers.HelperFunctions import getFromSplitArray
from repositories.Repository import Repository


class RefineryCostRepo(Repository[RefineryCost]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["RefineryCost"]

	@classmethod
	def generateRepo(cls) -> None:
		refSlots = getFromSplitArray(cls.getSection())
		for refSlot in refSlots:
			slotName = refSlot[12]
			cls.add(slotName, RefineryCost(cost = []))
			for i in range(6):
				if refSlot[i] == "Blank":
					continue
				cls.get(slotName).cost.append(Component(item = refSlot[i], quantity = refSlot[i + 6]))
