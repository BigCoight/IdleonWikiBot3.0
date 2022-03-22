from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.dungeons.DungEnemyRepo import DungEnemyRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.npc.NpcRepo import NpcRepo

newV = IdleonReader("151", True)
oldV = IdleonReader("150d", True)
# SpecificItemRepo.compareVersions(oldV, newV)
SourceRepo.initialise(newV.codeReader)
