from repositories.AnvilRepo import AnvilRepo
from repositories.BossDetailRepo import BossDetailRepo
from repositories.BubbleRepo import BubbleRepo
from repositories.BuildingRepo import BuildingRepo
from repositories.CardRepo import CardRepo
from repositories.CritterRepo import CritterRepo
from repositories.DropTableRepo import DropTableRepo
from repositories.FishingToolkitRepo import FishingToolkitRepo
from repositories.ItemDetailRepo import ItemDetailRepo
from helpers.CodeReader import CodeReader, IdelonReader
from repositories.MapNameRepo import MapNameRepo
from repositories.RecipeRepo import RecipeRepo
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
print(BubbleRepo.get("A Pair Of Gems"))
# print(CardRepository.repository)

print(FishingToolkitRepo.get("Weight1"))
