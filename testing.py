from helpers.CodeReader import IdleonReader
from repositories.npc.NpcRepo import NpcRepo

newV = IdleonReader("1561", True)
oldV = IdleonReader("156", True)
NpcRepo.initialise(newV.codeReader)
NpcRepo.exportWikiMult()
