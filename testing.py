# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.item.SpecificItemRepo import SpecificItemRepo

idleonReader = IdleonReader("alpha159", steam = True)
SpecificItemRepo.initialise(idleonReader.codeReader)
# ItemRepo.initialise(idleonReader.codeReader)
