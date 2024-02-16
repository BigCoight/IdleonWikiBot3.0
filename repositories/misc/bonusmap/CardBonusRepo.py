import re
from typing import List

from definitions.common.BonusMap import BonusMap
from repositories.master.Repository import Repository


class CardBonusRepo(Repository[BonusMap]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc/BonusMap"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["IdCardBonus"]

	@classmethod
	def generateRepo(cls) -> None:
		data = cls.getSection()
		reBonus = r'.\..\[(\d+)\] = \"(.+)?"'
		bonusMap = re.findall(reBonus, data)
		for bonusId, bonus in bonusMap:
			toAdd = BonusMap(id = bonusId, bonus = bonus)
			cls.add(f"{bonusId}", toAdd)
			cls.addList(toAdd)
