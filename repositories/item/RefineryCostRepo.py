from typing import List

from definitions.component.ComponentFactory import ComponentFactory
from definitions.misc.world3.RefineryCost import RefineryCost
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class RefineryCostRepo(Repository[RefineryCost]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["RefineryCost"]

	@classmethod
	def generateRepo(cls) -> None:
		refSlots = getFromSplitArray(cls.getSection())
		for refSlot in refSlots:
			slotName = refSlot[12]
			costs = []
			for i in range(6):
				if refSlot[i] == "Blank":
					continue
				costs.append(ComponentFactory.getComponent(refSlot[i], refSlot[i + 6]))
			cls.add(slotName, RefineryCost(cost = costs.copy()))
