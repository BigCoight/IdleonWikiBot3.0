from typing import List

from definitions.misc.world4.Meal import Meal
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class MealRepo(Repository[Meal]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MealInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			cls.addList(Meal.fromList(bonus))
			if cls.contains(bonus[0]): continue
			cls.add(bonus[0], Meal.fromList(bonus))

