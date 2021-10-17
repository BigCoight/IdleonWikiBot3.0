from helpers.CodeReader import IdelonReader
from repositories.AchievementRepo import AchievementRepo
from repositories.BubbleRepo import BubbleRepo
from repositories.BuildingRepo import BuildingRepo
from repositories.GemShopRepo import GemShopRepo
from repositories.MapNameRepo import MapNameRepo
from repositories.PostOfficeRepo import PostOfficeRepo
from repositories.PrayerRepo import PrayerRepo
from repositories.SaltLickRepo import SaltLickRepo
from repositories.ShrineRepo import ShrineRepo
from repositories.TaskUnlocksRepo import TaskUnlocksRepo
from repositories.arcade.ArcadeBonusRepo import ArcadeBonusRepo
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.collections.ItemRepo import ItemRepo
from repositories.dungeons.DungEnemyRepo import DungEnemyRepo
from repositories.dungeons.DungEnhanceRepo import DungEnhanceRepo
from repositories.dungeons.DungItemRepo import DungItemRepo
from repositories.dungeons.DungPassivesRepo import DungPassivesRepo
from repositories.dungeons.DungTraitRepo import DungTraitRepo
from repositories.dungeons.FlurboShopRepo import FlurboShopRepo
from repositories.dungeons.KeychainBonusRepo import KeychainBonusRepo
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.enemies.EnemyNavRepo import EnemyNavRepo
from repositories.enemies.EnemyTableRepo import EnemyTableRepo
from repositories.enemies.MapDataRepo import MapDataRepo
from repositories.enemies.SubTableRepo import SubTableRepo
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.CardRepo import CardRepo
from repositories.item.CritterRepo import CritterRepo
from repositories.item.FishingToolkitRepo import FishingToolkitRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.RefineryCostRepo import RefineryCostRepo
from repositories.item.SourceRepo import SourceRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.StatueRepo import StatueRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.npc.NpcHeadRepo import NpcHeadRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.npc.QuestNameRepo import QuestNameRepo
from repositories.talents.TalentNameRepo import TalentNameRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

idleonReader = IdelonReader("130")
codeReader = idleonReader.codeReader
EnemyDetailsRepo.initialise(codeReader)
CardRepo.initialise(codeReader)
ItemDetailRepo.initialise(codeReader)
StatueRepo.initialise(codeReader)
FishingToolkitRepo.initialise(codeReader)
SpecificItemRepo.initialise(codeReader)

# Arcade stuff
FlurboShopRepo.initialise(codeReader)
DungEnhanceRepo.initialise(codeReader)
ArcadeBonusRepo.initialise(codeReader)
AchievementRepo.initialise(codeReader)
DungTraitRepo.initialise(codeReader)
DungPassivesRepo.initialise(codeReader)
DungItemRepo.initialise(codeReader)
DungEnemyRepo.initialise(codeReader)
KeychainBonusRepo.initialise(codeReader)

MapNameRepo.initialise(codeReader)
MapDataRepo.initialise(codeReader)

VendorRepo.initialise(codeReader)
AnvilRepo.initialise(codeReader)
BossDetailRepo.initialise(codeReader)
BuildingRepo.initialise(codeReader)
BubbleRepo.initialise(codeReader)
CritterRepo.initialise(codeReader)
DropTableRepo.initialise(codeReader)
EnemyTableRepo.initialise(codeReader)
SubTableRepo.initialise(codeReader)
PostOfficeRepo.initialise(codeReader)
PrayerRepo.initialise(codeReader)
RefineryCostRepo.initialise(codeReader)
SaltLickRepo.initialise(codeReader)
ShrineRepo.initialise(codeReader)
GemShopRepo.initialise(codeReader)
RecipeRepo.initialise(codeReader)

TalentTreeRepo.initialise(codeReader)
TalentNameRepo.initialise(codeReader)
QuestNameRepo.initialise(codeReader)
NpcHeadRepo.initialise(codeReader)
NpcRepo.initialise(codeReader)
TaskUnlocksRepo.initialise(codeReader)

SourceRepo.initialise(codeReader)
EnemyNavRepo.initialise(codeReader)
EnemyRepo.initialise(codeReader)
ItemRepo.initialise(codeReader)

# print(DropTableRepo.get("SuperDropTable1").writeWiki())
print(ItemRepo.get("CardsX0").writeWiki())
# for item in ['EquipmentRings18', 'CardsX9', 'EquipmentPendant21', 'CardsX1', 'EquipmentHats67', 'CardsX13',
#              'CardsX16', 'ItemsCoupon2', 'CardsX12', 'CardsX5', 'CardsX4', 'EquipmentHats64', 'EquipmentPendant20',
#              'GemP13', 'CardsX0', 'Gfoodcoupon', 'CardsX15', 'Quest51', 'FoodHealth1d', 'Quest55', 'CardsX6',
#              'EquipmentHats65', 'CardsX8', 'EquipmentRings21', 'Quest53', 'LootDice', 'Cash', 'CardsX3', 'FoodHealth2d',
#              'XPskill', 'ItemsCoupon1', 'GemP11', 'EquipmentRings19', 'CardsX11', 'EquipmentPendant23', 'GemP15',
#              'EquipmentPendant19', 'XP', 'CardsX10', 'GemP14', 'BallJoePickle', 'CardsX7', 'Quest52',
#              'EquipmentRings22', 'SnowC5', 'EquipmentRings20', 'EquipmentHats66', 'CardsX2', 'CardsX14', 'GemP12',
#              'FoodHealth3d', 'Quest56', 'PalmTreeD', 'Quest54', 'CardPack4', 'GemP16', 'EquipmentPendant22']:
# 	dispName = SpecificItemRepo.get(item).displayName
# 	if SpecificItemRepo.get(item).Type in ["Dungeon Evaporate", "Currency", "Dungeon Food"]:
# 		continue
# 	with open(f"./test/{dispName}.txt", mode = 'w') as outfile:
# 		outfile.write(f"{dispName}\n {ItemRepo.get(item).writeWiki()}")
# 	print(ItemRepo.get(item).writeWiki()
ItemRepo.exportWikiMult()
