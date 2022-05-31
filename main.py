from helpers.CodeReader import IdleonReader
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
from repositories.enemies.EnemyNoteRepo import EnemyNoteRepo
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
from repositories.item.StampDescriptionRepo import StampDescriptionRepo
from repositories.item.StatueRepo import StatueRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.item.sources.CustomSourceRepo import CustomSourceRepo
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.misc.AchievementRepo import AchievementRepo
from repositories.misc.CardSetRepo import CardSetRepo
from repositories.misc.ConstellationsRepo import ConstellationsRepo
from repositories.misc.GemShopRepo import GemShopRepo
from repositories.misc.GuildBonusRepo import GuildBonusRepo
from repositories.misc.MapNameRepo import MapNameRepo
from repositories.misc.MapPortalsRepo import MapPortalsRepo
from repositories.misc.RandoListRepo import RandoListRepo
from repositories.misc.SkullShopRepo import SkullShopRepo
from repositories.misc.StarSignsRepo import StarSignsRepo
from repositories.misc.StorageOrderRepo import StorageOrderRepo
from repositories.misc.TaskDescriptionsRepo import TaskDescriptionRepo
from repositories.misc.TaskShopDescRepo import TaskShopDescRepo
from repositories.misc.TaskUnlocksRepo import TaskUnlocksRepo
from repositories.misc.world1.BribeRepo import BribeRepo
from repositories.misc.world2.BubbleRepo import BubbleRepo
from repositories.misc.world2.FishPoolRepo import FishPoolRepo
from repositories.misc.world2.PostOfficeRepo import PostOfficeRepo
from repositories.misc.world2.PostOfficeUpgradesRepo import PostOfficeUpgradesRepo
from repositories.misc.world2.SigilRepo import SigilRepo
from repositories.misc.world3.BuildingRepo import BuildingRepo
from repositories.misc.world3.PrayerRepo import PrayerRepo
from repositories.misc.world3.SaltLickRepo import SaltLickRepo
from repositories.misc.world3.ShrineRepo import ShrineRepo
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
from repositories.npc.NPCNoteRepo import NpcNoteRepo
from repositories.npc.NpcHeadRepo import NpcHeadRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.npc.QuestNameRepo import QuestNameRepo
from repositories.talents.TalentNameRepo import TalentNameRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

idleonReader = IdleonReader("158", steam = True)
# idleonReader = IdleonReader("123b", False)
codeReader = idleonReader.codeReader
CustomSourceRepo.initialise(codeReader)
EnemyDetailsRepo.initialise(codeReader)
CardRepo.initialise(codeReader)
ItemDetailRepo.initialise(codeReader)
StatueRepo.initialise(codeReader)
FishingToolkitRepo.initialise(codeReader)
KeychainBonusRepo.initialise(codeReader)
StorageOrderRepo.initialise(codeReader)
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

# Misc Repos
BribeRepo.initialise(codeReader)
GuildBonusRepo.initialise(codeReader)
StarSignsRepo.initialise(codeReader)

MapNameRepo.initialise(codeReader)
MapPortalsRepo.initialise(codeReader)
MapDataRepo.initialise(codeReader)
ConstellationsRepo.initialise(codeReader)

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
TaskDescriptionRepo.initialise(codeReader)
TaskShopDescRepo.initialise(codeReader)
PostOfficeUpgradesRepo.initialise(codeReader)

SourceRepo.initialise(codeReader)
ItemNoteRepo.initialise(codeReader)
EnemyNavRepo.initialise(codeReader)
EnemyNoteRepo.initialise(codeReader)
EnemyRepo.initialise(codeReader)
ItemRepo.initialise(codeReader)
StampDescriptionRepo.initialise(codeReader)
ArenaBonusRepo.initialise(codeReader)
ChipRepo.initialise(codeReader)
InfiniteTerritoryRepo.initialise(codeReader)
JewelRepo.initialise(codeReader)
LabBonusRepo.initialise(codeReader)
MealRepo.initialise(codeReader)
PetGeneRepo.initialise(codeReader)
PetStatRepo.initialise(codeReader)
PetUpgradeRepo.initialise(codeReader)
TerritoryFightRepo.initialise(codeReader)
FishPoolRepo.initialise(codeReader)
CardSetRepo.initialise(codeReader)
SigilRepo.initialise(codeReader)
SkullShopRepo.initialise(codeReader)

RandoListRepo.initialise(codeReader)
