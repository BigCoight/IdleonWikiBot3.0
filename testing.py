from helpers.CodeReader import IdleonReader
from repositories.misc.world4.ArenaBonusRepo import ArenaBonusRepo
from repositories.misc.world4.ChipRepo import ChipRepo
from repositories.misc.world4.InfiniteTerritoryRepo import InfiniteTerritoryRepo
from repositories.misc.world4.JewelRepo import JewelRepo
from repositories.misc.world4.LabBonusRepo import LabBonusRepo
from repositories.misc.world4.MealRepo import MealRepo
from repositories.misc.world4.PetGeneRepo import PetGeneRepo
from repositories.misc.world4.PetStatRepo import PetStatRepo
from repositories.misc.world4.PetUpgradeRepo import PetUpgradeRepo
from repositories.misc.world4.TerritoryFightRepo import TerritoryFightRepo

idleonReader = IdleonReader("150", True)
codeReader = idleonReader.codeReader

MealRepo.initialise(codeReader)
PetGeneRepo.initialise(codeReader)
PetStatRepo.initialise(codeReader)
TerritoryFightRepo.initialise(codeReader)
InfiniteTerritoryRepo.initialise(codeReader)
PetUpgradeRepo.initialise(codeReader)
LabBonusRepo.initialise(codeReader)
ArenaBonusRepo.initialise(codeReader)
ChipRepo.initialise(codeReader)
JewelRepo.initialise(codeReader)