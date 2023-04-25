from definitions.misc.world4.Pet import Pet, ShinyBonus
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository
from repositories.misc.RandoListRepo import RandoListRepo, RandoListDescriptions
from repositories.misc.world4.PetGeneRepo import PetGeneRepo
from repositories.misc.world4.PetStatRepo import PetStatRepo


class PetRepo(Repository[Pet]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def initDependencies(cls, log=True) -> None:
		RandoListRepo.initialise(cls.codeReader, False)
		PetGeneRepo.initialise(cls.codeReader, False)
		PetStatRepo.initialise(cls.codeReader, False)

	@classmethod
	def generateRepo(cls) -> None:
		for name, petStat in PetStatRepo.items():
			shinyBonusIndex = int(RandoListRepo.get(RandoListDescriptions.shinyBonusIndex)[petStat.unlockOrder])
			shinyBonusDesc = replaceUnderscores(RandoListRepo.get(RandoListDescriptions.shinyBonus)[shinyBonusIndex])
			shinyBonusPerLv = RandoListRepo.get(RandoListDescriptions.shinyBonusPerLvl)[shinyBonusIndex]
			petGeneIndex = int(RandoListRepo.get(RandoListDescriptions.petGeneticsDiscoverabilityOrder)[
				                   petStat.unlockOrder - 1])
			shinyBonus = ShinyBonus(shinyIndex=shinyBonusIndex, shinyBonusDesc=shinyBonusDesc,
			                        bonusPerLvl=shinyBonusPerLv)
			toAdd = Pet(stats=petStat, gene=PetGeneRepo.getList(petGeneIndex), shinyBonus=shinyBonus)
			cls.addList(toAdd)
			cls.add(name, toAdd)
