import re
from typing import List

from definitions.itemdef.FishingToolkit import FishingToolkit
from helpers.HelperFunctions import formatStr
from repositories.master.Repository import Repository


class FishingToolkitRepo(Repository[FishingToolkit]):

	@classmethod
	def parse(cls, value) -> FishingToolkit:
		return FishingToolkit.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["FishToolkit"]

	@classmethod
	def generateRepo(cls) -> None:
		fishingTKData = formatStr(cls.getSection(), ["  ", "\n"])
		section = re.split(r"],\[", fishingTKData)
		for n, v in enumerate(["Weight", "Line"]):
			tkData = re.findall(r'"([a-zA-Z0-9_ ]*)"\.', section[n])
			for i, tk in enumerate(tkData):
				data = tk.split(" ")
				cls.add(f"{v}{i}", FishingToolkit(
					name = data[0],
					depth1 = data[1],
					depth2 = data[2],
					depth3 = data[3],
					depth4 = data[4],
					fishingExp = data[5],
					fishingSpeed = data[6],
					fishingPower = data[7],
				))
