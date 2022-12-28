from typing import List

from definitions.common.QtylessComponent import QtylessComponent
from definitions.misc.world5.SlabItemSort import SlabItemSort
from helpers.HelperFunctions import getFromSplit
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class SlabItemSortRepo(Repository[SlabItemSort]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SlabItemSort"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplit(cls.getSection())
		for n, line in enumerate(data):
			cls.addList(SlabItemSort(order = n, item = QtylessComponent(item = line)))
			if cls.contains(line[0]): continue
			cls.add(line, SlabItemSort(order = n, item = QtylessComponent(item = line)))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return ItemDetailRepo.getDisplayName(name)
