from AllRepos import AllRepos
from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.collections.ItemRepo import ItemRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.misc.GemShopRepo import GemShopRepo
from repositories.misc.world5.SlabItemSortRepo import SlabItemSortRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

idleonReader = IdleonReader("2.27", steam = True)

for repo in AllRepos:
	repo.initialise(idleonReader.codeReader)

ItemRepo.initialise(idleonReader.codeReader)

ItemRepo.exportWikiMult()
NpcRepo.exportWikiMult()
EnemyRepo.exportWikiMult()
TalentTreeRepo.exportWikiMult()
DropTableRepo.exportWikiMult()
VendorRepo.exportWikiMult()
RecipeRepo.exportWikiMult()
GemShopRepo.exportWikiSingle()
SlabItemSortRepo.exportWikiSingle()
