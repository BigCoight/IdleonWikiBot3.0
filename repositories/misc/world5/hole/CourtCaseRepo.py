from typing import List

from definitions.misc.world5.hole.CourtCase import CaseOutcome, CourtCase
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class CourtCaseRepo(Repository[CourtCase]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def getOutcome(cls, lst: str) -> List[CaseOutcome]:
		if lst == "":
			return []
		outcomes = lst.split(".")
		res = []
		for outcome in outcomes:
			toAdd = CaseOutcome(
				category = outcome[0],
				qty = outcome[1:]
			)
			res.append(toAdd)
		return res

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection(), False)
		possibleNames = data[HoleOrder.PersonNames.value]
		cases = data[HoleOrder.JusticeCases.value]

		for n, case in enumerate(cases):
			currentCase = [replaceUnderscores(x) for x in case.split("|")]
			toAdd = CourtCase(
				person = replaceUnderscores(possibleNames[int(currentCase[0])]),
				desc = currentCase[1],
				approveOutcome = cls.getOutcome(currentCase[2]),
				rejectOutcome = cls.getOutcome(currentCase[3]),
				currencyScalePer5 = list(currentCase[4]),
				coincheck = currentCase[5]
			)
			cls.addList(toAdd)
			cls.add(f"{n}", toAdd)
