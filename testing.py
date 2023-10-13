# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world2.FishPoolRepo import FishPoolRepo

newV = IdleonReader("191", True)

FishPoolRepo.initialise(newV.codeReader)
