import string
from typing import List

from definitions.misc.world2.Sigil import Sigil
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class SigilRepo(Repository[Sigil]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SigilDesc"]

	@classmethod
	def generateRepo(cls) -> None:
		sigils = getFromSplitArray(cls.getSection())
		for sigil in sigils:
			sigil[0] = string.capwords(sigil[0])
			toAdd = Sigil.fromList(sigil)
			cls.add(sigil[0], toAdd)
			cls.addList(toAdd)
