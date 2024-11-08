from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonEnum import IdleonEnum


class ClassType(str, IdleonEnum, metaclass = CheckIn):
	"""
	Contains all class types
	"""
	All = "All"
	Mage = "Mage"
	Warrior = "Warrior"
	Beginner = "Beginner"
	Archer = "Archer"


class BagType(str, IdleonEnum, metaclass = CheckIn):
	"""
	Contains all types of material bags
	"""
	Foods = 'Foods'
	Chopping = 'Chopping'
	bCraft = 'bCraft'
	Critters = 'Critters'
	Souls = 'Souls'
	Bugs = 'Bugs'
	Fishing = 'Fishing'
	Mining = 'Mining'


class TypeGen(str, IdleonEnum, metaclass = CheckIn):
	"""
	Contains all current types
	"""
	NothingERROR = 'NothingERROR'
	aShoes = 'aShoes'
	dStone = 'dStone'
	aPants = 'aPants'
	aWeapon = 'aWeapon'
	aShirt = 'aShirt'
	aChatRingMTX = 'aChatRingMTX'
	aTrap = 'aTrap'
	dFish = 'dFish'
	bLeaf = 'bLeaf'
	dCardPack = 'dCardPack'
	dCard = 'dCard'
	dTimeCandy = 'dTimeCandy'
	aObolCircle = 'aObolCircle'
	aObolSparkle = 'aObolSparkle'
	dExpOrb = "dExpOrb"
	aPick = 'aPick'
	cOil = 'cOil'
	dSouls = 'dSouls'
	aPendant = 'aPendant'
	bBar = 'bBar'
	aHatchet = 'aHatchet'
	dBugs = 'dBugs'
	aBugNet = 'aBugNet'
	aSkull = 'aSkull'
	dQuest = 'dQuest'
	bCraft = 'bCraft'
	dFishToolkit = 'dFishToolkit'
	aHelmetMTX = 'aHelmetMTX'
	cFood = 'cFood'
	dStatueStone = 'dStatueStone'
	aRecipe = 'aRecipe'
	aTalentBook = 'aTalentBook'
	dCurrency = 'dCurrency'
	aCarryBag = 'aCarryBag'
	bLog = 'bLog'
	aStorageChest = 'aStorageChest'
	aStamp = 'aStamp'
	aRing = 'aRing'
	aInventoryBag = 'aInventoryBag'
	bOre = 'bOre'
	aTrophy = 'aTrophy'
	aHelmet = 'aHelmet'
	aObolSquare = 'aObolSquare'
	aObolHexagon = 'aObolHexagon'
	aFishingRod = 'aFishingRod'
	dCritters = 'dCritters'
	aError = 'aError'
	aKeychain = 'aKeychain'
	aCape = 'aCape'
	aDNAgun = "aDNAgun"
	aNametag = "aNametag"
	aGown = "aGown"
