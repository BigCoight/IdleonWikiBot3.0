from helpers.CodeReader import IdelonReader
from repositories.AnvilRepo import AnvilRepo
from repositories.BossDetailRepo import BossDetailRepo
from repositories.BubbleRepo import BubbleRepo
from repositories.BuildingRepo import BuildingRepo
from repositories.CardRepo import CardRepo
from repositories.CritterRepo import CritterRepo
from repositories.DropTableRepo import DropTableRepo
from repositories.EnemyRepo import EnemyRepo
from repositories.FishingToolkitRepo import FishingToolkitRepo
from repositories.GemShopRepo import GemShopRepo
from repositories.ItemDetailRepo import ItemDetailRepo
from repositories.MapNameRepo import MapNameRepo
from repositories.PostOfficeRepo import PostOfficeRepo
from repositories.PrayerRepo import PrayerRepo
from repositories.RecipeRepo import RecipeRepo
from repositories.RefineryCostRepo import RefineryCostRepo
from repositories.SaltLickRepo import SaltLickRepo
from repositories.ShrineRepo import ShrineRepo
from repositories.StatueRepo import StatueRepo
from repositories.TalentNameRepo import TalentNameRepo
from repositories.TalentTreeRepo import TalentTreeRepo
from repositories.VendorRepo import VendorRepo

idleonReader = IdelonReader("idleon123b.txt")
codeReader = idleonReader.codeReader

ItemDetailRepo.initialise(codeReader)
MapNameRepo.initialise(codeReader)
RecipeRepo.initialise(codeReader)
CardRepo.initialise(codeReader)
VendorRepo.initialise(codeReader)
FishingToolkitRepo.initialise(codeReader)
AnvilRepo.initialise(codeReader)
BossDetailRepo.initialise(codeReader)
BuildingRepo.initialise(codeReader)
BubbleRepo.initialise(codeReader)
CritterRepo.initialise(codeReader)
DropTableRepo.initialise(codeReader)
EnemyRepo.initialise(codeReader)
PostOfficeRepo.initialise(codeReader)
PrayerRepo.initialise(codeReader)
RefineryCostRepo.initialise(codeReader)
SaltLickRepo.initialise(codeReader)
ShrineRepo.initialise(codeReader)
GemShopRepo.initialise(codeReader)
StatueRepo.initialise(codeReader)
TalentTreeRepo.initialise(codeReader)
TalentNameRepo.initialise(codeReader)
print(BubbleRepo.get("A Pair Of Gems"))
# print(CardRepository.repository)

print(FishingToolkitRepo.get("Weight1"))
