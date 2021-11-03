from helpers.CodeReader import IdleonReader
from repositories.AchievementRepo import AchievementRepo
from repositories.BribeRepo import BribeRepo
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
from repositories.item.DetDropsRepo import DetDropsRepo
from repositories.item.FishingToolkitRepo import FishingToolkitRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.RefineryCostRepo import RefineryCostRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.StatueRepo import StatueRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.item.sources.CustomSourceRepo import CustomSourceRepo
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.item.sources.WikiSourceRepo import WikiSourceRepo
from repositories.npc.NPCNoteRepo import NpcNoteRepo
from repositories.npc.NpcHeadRepo import NpcHeadRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.npc.QuestNameRepo import QuestNameRepo
from repositories.talents.TalentNameRepo import TalentNameRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

idleonReader = IdleonReader("steam130b", True)
# idleonReader = IdleonReader("123b", False)
codeReader = idleonReader.codeReader
CustomSourceRepo.initialise(codeReader)
EnemyDetailsRepo.initialise(codeReader)
CardRepo.initialise(codeReader)
ItemDetailRepo.initialise(codeReader)
StatueRepo.initialise(codeReader)
FishingToolkitRepo.initialise(codeReader)
KeychainBonusRepo.initialise(codeReader)
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
BribeRepo.initialise(codeReader)

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
DetDropsRepo.initialise(codeReader)
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
NpcNoteRepo.initialise(codeReader)
TaskUnlocksRepo.initialise(codeReader)

SourceRepo.initialise(codeReader)
WikiSourceRepo.initialise(codeReader)
ItemNoteRepo.initialise(codeReader)
EnemyNavRepo.initialise(codeReader)
EnemyRepo.initialise(codeReader)
ItemRepo.initialise(codeReader)

BribeRepo.compareVersions(IdleonReader("130"), IdleonReader("steam130b", True))
