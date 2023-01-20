from helpers.CodeReader import IdleonReader
from repositories.arcade.ArcadeBonusRepo import ArcadeBonusRepo
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.dungeons.DungEnemyRepo import DungEnemyRepo
from repositories.dungeons.DungItemRepo import DungItemRepo
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.RefineryCostRepo import RefineryCostRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.TrapBoxRepo import TrapBoxRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.misc.AchievementRepo import AchievementRepo
from repositories.misc.CardSetRepo import CardSetRepo
from repositories.misc.ColosseumRepo import ColosseumRepo
from repositories.misc.ConstellationsRepo import ConstellationsRepo
from repositories.misc.GemShopRepo import GemShopRepo
from repositories.misc.GuildBonusRepo import GuildBonusRepo
from repositories.misc.TaskShopDescRepo import TaskShopDescRepo
from repositories.misc.world1.BribeRepo import BribeRepo
from repositories.misc.world2.BubbleRepo import BubbleRepo
from repositories.misc.world2.FishPoolRepo import FishPoolRepo
from repositories.misc.world2.PostOfficeRepo import PostOfficeRepo
from repositories.misc.world2.PostOfficeUpgradesRepo import PostOfficeUpgradesRepo
from repositories.misc.world2.SigilRepo import SigilRepo
from repositories.misc.world3.BuildingRepo import BuildingRepo
from repositories.misc.world3.PrayerRepo import PrayerRepo
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
from repositories.misc.world5.ArtifactRepo import ArtifactRepo
from repositories.misc.world5.CaptainBonusRepo import CaptainBonusRepo
from repositories.misc.world5.DivinityStyleRepo import DivinityStyleRepo
from repositories.misc.world5.GamingBoxRepo import GamingBoxRepo
from repositories.misc.world5.GamingUpgradeRepo import GamingUpgradeRepo
from repositories.misc.world5.GodInfoRepo import GodInfoRepo
from repositories.misc.world5.IslandInfoRepo import IslandInfoRepo
from repositories.misc.world5.SlabItemSortRepo import SlabItemSortRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

newV = IdleonReader("173", True)
oldV = IdleonReader("172", True)

SpecificItemRepo.compareVersions(oldV, newV)
EnemyRepo.compareVersions(oldV, newV)
DropTableRepo.compareVersions(oldV, newV)
NpcRepo.compareVersions(oldV, newV)
RecipeRepo.compareVersions(oldV, newV)
BubbleRepo.compareVersions(oldV, newV)
TalentTreeRepo.compareVersions(oldV, newV)
PostOfficeUpgradesRepo.compareVersions(oldV, newV)
PostOfficeRepo.compareVersions(oldV, newV)
VendorRepo.compareVersions(oldV, newV)
PrayerRepo.compareVersions(oldV, newV)
GemShopRepo.compareVersions(oldV, newV)
BuildingRepo.compareVersions(oldV, newV)
ShrineRepo.compareVersions(oldV, newV)
RefineryCostRepo.compareVersions(oldV, newV)
BribeRepo.compareVersions(oldV, newV)
ConstellationsRepo.compareVersions(oldV, newV)
DungEnemyRepo.compareVersions(oldV, newV)
DungItemRepo.compareVersions(oldV, newV)
AchievementRepo.compareVersions(oldV, newV)
GuildBonusRepo.compareVersions(oldV, newV)
AnvilRepo.compareVersions(oldV, newV)

ArenaBonusRepo.compareVersions(oldV, newV)
ChipRepo.compareVersions(oldV, newV)
InfiniteTerritoryRepo.compareVersions(oldV, newV)

JewelRepo.compareVersions(oldV, newV)
LabBonusRepo.compareVersions(oldV, newV)
MealRepo.compareVersions(oldV, newV)

PetGeneRepo.compareVersions(oldV, newV)
PetStatRepo.compareVersions(oldV, newV)
PetUpgradeRepo.compareVersions(oldV, newV)

TerritoryFightRepo.compareVersions(oldV, newV)
BossDetailRepo.compareVersions(oldV, newV)
CardSetRepo.compareVersions(oldV, newV)
FishPoolRepo.compareVersions(oldV, newV)
TrapBoxRepo.compareVersions(oldV, newV)
ArcadeBonusRepo.compareVersions(oldV, newV)
SigilRepo.compareVersions(oldV, newV)

TaskShopDescRepo.compareVersions(oldV, newV)
ColosseumRepo.compareVersions(oldV, newV)

ArtifactRepo.compareVersions(oldV, newV)
CaptainBonusRepo.compareVersions(oldV, newV)
DivinityStyleRepo.compareVersions(oldV, newV)
GamingBoxRepo.compareVersions(oldV, newV)
GamingUpgradeRepo.compareVersions(oldV, newV)
GodInfoRepo.compareVersions(oldV, newV)
IslandInfoRepo.compareVersions(oldV, newV)
SlabItemSortRepo.compareVersions(oldV, newV)
