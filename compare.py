from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.misc.GemShopRepo import GemShopRepo
from repositories.misc.world2.BubbleRepo import BubbleRepo
from repositories.misc.world2.PostOfficeRepo import PostOfficeRepo
from repositories.misc.world2.PostOfficeUpgradesRepo import PostOfficeUpgradesRepo
from repositories.misc.world3.PrayerRepo import PrayerRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

newV = IdleonReader("150", True)
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