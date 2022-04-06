from copy import deepcopy
from typing import List, Set

from definitions.arcade.ArcadeBonus import ArcadeBonus
from helpers.CodeReader import IdleonReader
from helpers.ColourPrinter import printYellow
from helpers.HelperFunctions import getFromSplitArray
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.master.Repository import Repository


class ArcadeBonusRepo(Repository[ArcadeBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Arcade"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ArcadeBonus"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, bonus in enumerate(data):
			toAdd = ArcadeBonus.fromList(bonus)
			cls.add(f"Bonus {n}", toAdd)
			cls.addList(toAdd)

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set()):
		"""

		Args:
			v1: The version that is "Old"
			v2: The version that is "New"
			ignored: A set of attributes to ignore in the comparison

		Returns:
		"""

		changes = {}
		new = {}
		cr1 = v1.codeReader
		cr2 = v2.codeReader

		cls.initialise(cr1, False)
		repo1 = deepcopy(cls.repository)
		cls.initialise(cr2, False)
		repo2 = deepcopy(cls.repository)
		key1 = set(repo1.keys())
		key2 = set(repo2.keys())

		sameItems = key1.intersection(key2)
		newItems = key2 - key1
		for sameItem in sameItems:
			if cls._ignore(sameItem, repo2[sameItem]):
				continue
			if repo1[sameItem].isFiller():
				newItems.add(sameItem)
				continue
			if repo1[sameItem].compare(repo2[sameItem], ignored):
				newItems.add(sameItem)

		for newItem in newItems:
			if cls._ignore(newItem, repo2[newItem]):
				continue
			new[newItem] = repo2[newItem].toDict(ignored)

		out = {
			"new": new,
			"changes": changes
		}
		changeName = cls._getPath("changes", "json")
		with open(changeName, mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(out))
		cls._writeChangesWiki(out)

		if len(new) == 0 and len(changes) == 0:
			return

		printYellow(f"Compared {cls.__name__} with {len(new)} new items and {len(changes)} changes")
