import re
from typing import List

from definitions.itemdef.AnvilProduce import AnvilProduce
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class AnvilRepo(Repository[AnvilProduce]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Production"]

	@classmethod
	def generateRepo(cls) -> None:
		reProd = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		items = re.findall(reProd, cls.getSection())
		for n, item in enumerate(items):
			toAdd = AnvilProduce(
				item = item[0],
				no = n + 1,
				time = item[1],
				levelReq = item[2],
				exp = item[3]
			)
			cls.add(item[0], toAdd)
			cls.addList(toAdd)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return ItemDetailRepo.getWikiName(name)
