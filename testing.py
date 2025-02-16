# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.item.SpecificItemRepo import SpecificItemRepo

newV = IdleonReader("2.28", True)

SpecificItemRepo.initialise(newV.codeReader)
