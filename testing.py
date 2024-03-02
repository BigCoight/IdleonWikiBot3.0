# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world1.BribeRepo import BribeRepo

newV = IdleonReader("202", True)
oldV = IdleonReader("201", True)

BribeRepo.compareVersions(oldV, newV)
