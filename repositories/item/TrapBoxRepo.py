from typing import List

from definitions.itemdef.Critter import Critter
from definitions.misc.world3.TrapBox import TrapBox, TrapBoxTime
from helpers.HelperFunctions import getFromSplitArray, getFrom4dArray
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.misc.MapNameRepo import MapNameRepo
from repositories.master.Repository import Repository


class TrapBoxRepo(Repository[TrapBox]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TrapBox"]

	@classmethod
	def generateRepo(cls) -> None:
		trapBoxes = getFrom4dArray(cls.getSection())[0]
		for n, trapBox in enumerate(trapBoxes):
			times = []
			for time in trapBox:
				times.append(TrapBoxTime(
					time =time[0],
					qtyX =time[1],
					expX =time[2] if time[3] == "0" else 0,
					shinyX =time[2] if time[3] == "1" else 0))
			cls.addList(TrapBox(times = times.copy()))
			cls.add(f"TrapBoxSet{n+1}", TrapBox(times = times.copy()))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return ItemDetailRepo.getWikiName(name)

	@classmethod
	def _extractWikiSingle(cls) -> str:
		res = "{{Traps/head}}\n"
		for name, trapBox in cls.items():
			res += "{{Traps/row"+f"|name={cls.getWikiName(name)}|rowspan={len(trapBox.times)}"
			res += trapBox.writeWikiSingle()
		res += "|}"
		return res
