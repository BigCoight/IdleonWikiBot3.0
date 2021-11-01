import re
from typing import List

from definitions.itemdef.AnvilProduce import AnvilProduce
from repositories.master.Repository import Repository


class AnvilRepo(Repository[AnvilProduce]):
	@classmethod
	def getSections(cls) -> List[str]:
		return ["Production"]

	@classmethod
	def generateRepo(cls) -> None:
		reProd = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		items = re.findall(reProd, cls.getSection())
		for n, item in enumerate(items):
			cls.add(item[0], AnvilProduce(
				no = n + 1,
				time = item[1],
				levelReq = item[2],
				exp = item[3]
			))
