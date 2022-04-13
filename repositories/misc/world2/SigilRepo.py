import re
from typing import List

from definitions.common.LiquidComponent import LiquidComponent
from definitions.misc.world2.Bubble import Bubble
from definitions.common.Component import Component
from definitions.misc.world2.Sigil import Sigil
from helpers.HelperFunctions import replaceUnderscores, camelCaseToTitle, getFromSplitArray
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
			toAdd = Sigil.fromList(sigil)
			cls.add(sigil[0], toAdd)
			cls.addList(toAdd)