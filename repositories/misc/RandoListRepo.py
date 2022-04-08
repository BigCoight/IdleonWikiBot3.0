from enum import Enum, auto

from definitions.common.EnumMeta import CheckIn
from definitions.misc.RandoList import RandoList
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository
from typing import List, Optional


class RandoListDescriptions(int, Enum, metaclass= CheckIn):
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


class RandoListRepo(Repository[RandoList]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["RandoList"]

	@classmethod
	def generateRepo(cls) -> None:
		lsts = getFromSplitArray(cls.getSection())
		for n, lst in enumerate(lsts):
			cls.addList(RandoList(elements = lst))
			cls.add(RandoListDescriptions(n+1).name, RandoList(elements = lst))

	@classmethod
	def get(cls, key: RandoListDescriptions) -> Optional[RandoList]:
		return super().get(key.name)
