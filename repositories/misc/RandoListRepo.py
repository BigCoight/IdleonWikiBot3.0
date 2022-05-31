import re
from enum import auto
from typing import List, Optional

from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonEnum import IdleonEnum
from definitions.misc.RandoList import RandoList
from helpers.HelperFunctions import strToArray
from repositories.master.Repository import Repository


class RandoListDescriptions(int, IdleonEnum, metaclass = CheckIn):
	monstersInGrasslands = auto()
	monstersInDesert = auto()
	noItemsRemoveFromAnvTab1 = auto()
	noItemsRemoveFromAnvTab2 = auto()
	typesOfHelmetStats = auto()
	randomMobsThatCanSpawn = auto()
	startFrameBoxTrap = auto()
	boxTrapCategory = auto()
	xYOfOrbs = auto()
	wizardLvPrayerSlot = auto()
	tdAreas = auto()
	cogLvReq = auto()
	cogBuildingReq = auto()
	towerBuildingPart = auto()
	unbuiltTowerDesc = auto()
	monstersInSnow = auto()
	talentIdsNotInLib = auto()
	lootyIgnore = auto()
	refPowerQtyLvlUp = auto()
	npcsInBlunder = auto()
	npcsInYumyum = auto()
	npcsInFrostbite = auto()
	obolStack1 = auto()
	obolStack2 = auto()
	numbers = auto()
	typesOfItemsInAccount1 = auto()
	typesOfItemsInAccount2 = auto()
	xValueForDungeons = auto()
	itemsHoldToUseAll = auto()
	dcreditsToRank = auto()
	xYOfDungLocks = auto()
	lettersRecalibrate = auto()
	nodeTravelInfoForMafiosoBoss = auto()
	randomOrderOfGapsFireDungeon = auto()
	xYOfArcadeLights = auto()
	xYOfArcadeSpinners = auto()
	securityForFrogDungeon = auto()
	prefixDungItems = auto()
	idAttacksOthersCanSee = auto()
	itemsHoldToUseOne = auto()
	resourceBag1 = auto()
	resourceBag2 = auto()
	maxLvForgeUpgrades = auto()
	idAttacksPartyDungeons = auto()
	idTalentBooksFromFlurbo = auto()
	idT1Keychains = auto()
	idT2Keychains = auto()
	idT3Keychains = auto()
	idArcadeRewards = auto()
	idUniqueRecipeSpices = auto()
	specificRecipeOdds = auto()
	barExpBarChange = auto()
	petTerritoryCurrentMap = auto()
	roundForPetUnlockBonus = auto()
	baseChanceBreedingId = auto()
	petGeneticsDiscoverabilityOrder = auto()
	rngOrderChips = auto()
	vipMembershipStarTalent = auto()
	npcsInNebulon = auto()
	qtyOfTrappingMinigameBonus = auto()
	idk1 = auto()
	patchNotes = auto()
	idk3 = auto()
	idk4 = auto()
	idk5 = auto()
	idk6 = auto()
	idk7 = auto()
	idk8 = auto()
	idk9 = auto()
	idk10 = auto()
	idk11 = auto()
	idk12 = auto()
	idk13 = auto()
	idk14 = auto()
	idk15 = auto()


class RandoListRepo(Repository[RandoList]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["RandoList"]

	@classmethod
	def generateRepo(cls) -> None:
		section = cls.getSection().replace("return [", "")
		print(section)
		lsts = re.findall(fr'(?:"(.*?)"\.split|\[((?:.|\n)*?)\])', section)
		for n, lst in enumerate(lsts):
			if lst[0]:
				if " " in lst[0]:
					cls.addList(RandoList(elements = lst[0].split(" ")))
					cls.add(RandoListDescriptions(n + 1).name, RandoList(elements = lst[0].split(" ")))
				else:
					cls.addList(RandoList(elements = list(lst[0])))
					cls.add(RandoListDescriptions(n + 1).name, RandoList(elements = list(lst[0])))
			else:
				cls.addList(RandoList(elements = strToArray(lst[1])))
				cls.add(RandoListDescriptions(n + 1).name, RandoList(elements = strToArray(lst[1])))

	@classmethod
	def get(cls, key: RandoListDescriptions) -> Optional[RandoList]:
		if isinstance(key, str):
			return super().get(key)
		return super().get(key.name)
