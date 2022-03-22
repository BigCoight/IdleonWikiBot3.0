import re
from typing import List

from definitions.postoffice.PostOffice import PostOffice, Part
from helpers.Constants import Constants
from helpers.HelperFunctions import formatStr, wrap, strToArray
from repositories.master.Repository import Repository


class PostOfficeRepo(Repository[PostOffice]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def parse(cls, value) -> PostOffice:
		return PostOffice.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PostOffice"]

	@classmethod
	def generateRepo(cls) -> None:
		postData = formatStr(cls.getSection(), ["\n", "  "])
		postOffices = [wrap(x) for x in re.split(r"],?],?],\[\[\[", postData)]
		for j, postOffice in enumerate(postOffices):
			if j >= len(Constants.postNames):
				break
			category = [wrap(x) for x in re.split(r",?],?],\[\[", postOffice)]
			parts = {"Orders": [], "Rewards": []}
			coins = []
			for n, v in enumerate(parts.keys()):
				itemData = re.split(r"],\[", category[n])
				for item in itemData:
					data = strToArray(item)
					if len(data) > 3:
						coins = data
						continue
					if len(data) != 3: continue #Lava needs to fix this
					parts[v].append(Part(
						item = data[0],
						base = data[1],
						increment = data[2],
					))
			cls.add(Constants.postNames[j], PostOffice(
				orders = parts["Orders"].copy(),
				coinRewards = coins.copy(),
				rewards = parts["Rewards"].copy(),
			))
