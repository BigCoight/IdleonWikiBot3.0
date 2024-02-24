# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world2.BubbleRepo import BubbleRepo

newV = IdleonReader("200", True)
oldV = IdleonReader("192", True)

BubbleRepo.compareVersions(oldV, newV)
