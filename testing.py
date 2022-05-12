from helpers.CodeReader import IdleonReader
from repositories.dungeons.DungItemRepo import DungItemRepo

newV = IdleonReader("1561", True)
oldV = IdleonReader("156", True)
DungItemRepo.compareVersions(oldV, newV)
