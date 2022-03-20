from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.dungeons.DungEnemyRepo import DungEnemyRepo
from repositories.dungeons.DungItemRepo import DungItemRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.RefineryCostRepo import RefineryCostRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.misc.AchievementRepo import AchievementRepo
from repositories.misc.ConstellationsRepo import ConstellationsRepo
from repositories.misc.GemShopRepo import GemShopRepo
from repositories.misc.GuildBonusRepo import GuildBonusRepo
from repositories.misc.world1.BribeRepo import BribeRepo
from repositories.misc.world2.BubbleRepo import BubbleRepo
from repositories.misc.world2.PostOfficeRepo import PostOfficeRepo
from repositories.misc.world2.PostOfficeUpgradesRepo import PostOfficeUpgradesRepo
from repositories.misc.world3.BuildingRepo import BuildingRepo
from repositories.misc.world3.PrayerRepo import PrayerRepo
from repositories.misc.world3.ShrineRepo import ShrineRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

newV = IdleonReader("150d", True)
oldV = IdleonReader("140b", True)

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

