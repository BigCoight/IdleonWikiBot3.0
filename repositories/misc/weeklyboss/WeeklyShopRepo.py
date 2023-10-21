from typing import List

from definitions.misc.weeklybosses.WeeklyShop import WeeklyShop, WeeklyShopSection
from helpers.HelperFunctions import getFrom4dArray
from repositories.master.Repository import Repository


class WeeklyShopRepo(Repository[WeeklyShop]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc/WeeklyTask"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["WeeklyShop"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFrom4dArray(cls.getSection())
		for sectN, items in zip([WeeklyShopSection.UI, WeeklyShopSection.Items], data[0]):
			for item in items:
				toAdd = WeeklyShop(
					name = item[0],
					section = sectN,
					cost = item[1],
					intName = item[2],
					desc = item[3],
					itemType = item[4]
				)
				cls.addList(toAdd)
				cls.add(item[0], toAdd)
