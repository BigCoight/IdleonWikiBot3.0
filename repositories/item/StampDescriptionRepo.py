from definitions.itemdef.StampDescription import StampDescription
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository
from typing import List


class StampDescriptionRepo(Repository[StampDescription]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["StampDescriptions"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, descs in enumerate(data):
			cls.add(Constants.stampTypes[n], StampDescription(descriptions=descs))
