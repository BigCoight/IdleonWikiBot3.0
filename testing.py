# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world5.hole.AmplifierStoneRepo import AmplifierStoneRepo

newV = IdleonReader("2.23", True)

AmplifierStoneRepo.initialise(newV.codeReader)
