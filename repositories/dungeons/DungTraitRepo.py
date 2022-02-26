from typing import List

from definitions.dungeons.DungTrait import DungSet, DungTrait
from helpers.HelperFunctions import replaceUnderscores, getFromSplit
from repositories.master.Repository import Repository


class DungTraitRepo(Repository[DungSet]):
	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungTraits"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplit(cls.getSection())
		cls.add(
			"Beginner Traits",
			DungSet(
				name="Beginner Traits",
				rankReq=5,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[0:3]],
			),
		)

		cls.add(
			"Kinda Cool Traits",
			DungSet(
				name="Kinda Cool Traits",
				rankReq=10,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[3:6]],
			),
		)

		cls.add(
			"Strategery Traits",
			DungSet(
				name="Strategery Traits",
				rankReq=15,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[6:10]],
			),
		)

		cls.add(
			"Da Cred Traits",
			DungSet(
				name="Da Cred Traits",
				rankReq=20,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[10:12]],
			),
		)

		cls.add(
			"Drop Drip Traits",
			DungSet(
				name="Drop Drip Traits",
				rankReq=25,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[12:16]],
			),
		)

		cls.add(
			"Cash Money Traits",
			DungSet(
				name="Cash Money Traits",
				rankReq=30,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[16:19]],
			),
		)

		cls.add(
			"ChOiIiCe Traits",
			DungSet(
				name="ChOiIiCe Traits",
				rankReq=35,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[19:22]],
			),
		)

		cls.add(
			"Royale Traits",
			DungSet(
				name="Royale Traits",
				rankReq=40,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[22:24]],
			),
		)

		cls.add(
			"Endothelium Traits",
			DungSet(
				name="Endothelium Traits",
				rankReq=50,
				traits=[DungTrait(name=replaceUnderscores(trait)) for trait in data[24:28]],
			),
		)