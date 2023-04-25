import re
from enum import auto
from typing import List, Optional

from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonEnum import IdleonEnum
from definitions.misc.RandoList import RandoList
from helpers.HelperFunctions import strToArray
from repositories.master.Repository import Repository


class RandoListDescriptions(int, IdleonEnum, metaclass=CheckIn):
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
	animationsForPopup = auto()
	patchNotes = auto()
	petsForTaskW4ID2 = auto()
	mealsForTaskW4ID0 = auto()
	testListObj = auto()
	monstersBossHpBar = auto()
	classNotOut = auto()
	classNotOut2 = auto()
	killroyRoomsW1 = auto()
	killroyRoomsW2 = auto()
	killroyRoomsW3 = auto()
	killroyRoomsW4 = auto()
	killroyRoomsW5 = auto()
	trollBossOpeners = auto()
	trollMinigames = auto()
	trollDying = auto()
	converterGeneticAttacks = auto()
	bossObols = auto()
	xYOfMutationDisplay = auto()
	npcsInSmolderin = auto()
	dk1 = auto()
	dk2 = auto()
	dk3 = auto()
	dk4 = auto()
	dk5 = auto()
	dk6 = auto()
	dk7 = auto()
	dk8 = auto()
	dk9 = auto()
	dk10 = auto()
	shinyBonusIndex = auto()
	shinyBonus = auto()
	shinyBonusPerLvl = auto()
	dk14 = auto()
	dk15 = auto()
	dk16 = auto()
	dk17 = auto()
	dk18 = auto()


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
		lsts = re.findall(fr'(?:"(.*?)"\.split|\[((?:.|\n)*?)\])', section)
		for n, lst in enumerate(lsts):
			if lst[0]:
				if " " in lst[0]:
					cls.addList(RandoList(elements=lst[0].split(" ")))
					cls.add(RandoListDescriptions(n + 1).name, RandoList(elements=lst[0].split(" ")))
				else:
					cls.addList(RandoList(elements=list(lst[0])))
					cls.add(RandoListDescriptions(n + 1).name, RandoList(elements=list(lst[0])))
			else:
				cls.addList(RandoList(elements=strToArray(lst[1])))
				cls.add(RandoListDescriptions(n + 1).name, RandoList(elements=strToArray(lst[1])))

	@classmethod
	def get(cls, key: RandoListDescriptions) -> Optional[RandoList]:
		if isinstance(key, str):
			return super().get(key)
		return super().get(key.name)
