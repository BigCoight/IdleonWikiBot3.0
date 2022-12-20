from typing import List

from definitions.misc.world5.Artifact import Artifact
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ArtifactRepo(Repository[Artifact]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ArtifactInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(Artifact.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], Artifact.fromList(line))
