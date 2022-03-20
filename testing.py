from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo


newV = IdleonReader("150d", True)
oldV = IdleonReader("140b", True)
EnemyRepo.compareVersions(oldV, newV)
