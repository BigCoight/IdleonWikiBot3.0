from typing import List, Dict

from definitions.misc.GrimoireUpgrade import GrimoireUpgrade
from helpers.HelperFunctions import replaceUnderscores, getFromSplitArray
from repositories.master.Repository import Repository


class GrimoireUpgradeRepo(Repository[GrimoireUpgrade]):
	# Mapping of upgrade index to tooltip text from the UI code
	# Based on the game's UI code
	TOOLTIP_TEXTS: Dict[int, str] = {
		0: "Enter Wraith Form using the other Talent. It lets you get bones from killing monsters! Exit Wraith Form by reusing the talent.",
		5: "You only get ribbons on days you play IdleOn. If your Shelf is full, the new ribbon will try to combine with another.",
		13: "A Knockout, or KO, is when you kill the target monster in a single hit using your bare hands, no spears allowed!",
		21: "An Elimination is when you defeat the entire map of target monsters before any of them respawn!",
		31: "An Annihilation is when you defeat 200 target monsters within 60 seconds of entering their map!",
		24: "This bonus affects all your players, all the time! It has nothing to do with Wraith Form or your Death Bringer.",
		35: "This bonus affects all your players, all the time! It has nothing to do with Wraith Form or your Death Bringer.",
		39: "This bonus affects all your players, all the time! It has nothing to do with Wraith Form or your Death Bringer.",
		44: "This bonus affects all your players, all the time! It has nothing to do with Wraith Form or your Death Bringer."
	}

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GrimoireUpg"]

	@classmethod
	def generateRepo(cls) -> None:
		grimoire_data = getFromSplitArray(cls.getSection())

		for index, data in enumerate(grimoire_data):
			if not data or len(data) < 10:  # We need at least 10 fields
				continue

			name = data[0]
			has_tooltip = "製" in name
			
			# Clean up the name by removing the tooltip indicator
			if has_tooltip:
				charIndex = name.index("製")
				name = name[0:charIndex].rstrip()

			# Mapping based on game's UI code:
			# data[0] is name
			# data[1] is base_cost
			# data[2] is scaling_factor
			# data[3] is x1 (unknown purpose)
			# data[4] is max_level
			# data[5] is value
			# data[6] is unlock_req
			# data[8] is x2 (unknown purpose)
			# data[9] is description

			# Get tooltip text if it exists for this index
			tooltip_text = cls.TOOLTIP_TEXTS.get(index)

			upgrade = GrimoireUpgrade(
				name = name,
				base_cost = data[1],
				scaling_factor = data[2],
				x1 = data[3],
				max_level = data[4],
				value = data[5],
				unlock_req = data[6],
				x2 = data[8],
				description = data[9],
				has_tooltip = has_tooltip,
				tooltip_text = tooltip_text
			)

			cls.add(name, upgrade)
			cls.addList(upgrade) 