from typing import List

from definitions.misc.world3.AtomCollider import AtomCollider
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class AtomColliderRepo(Repository[AtomCollider]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/3"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["AtomInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(AtomCollider.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], AtomCollider.fromList(line))
