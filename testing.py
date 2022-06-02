# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.misc.RandoListRepo import RandoListRepo

idleonReader = IdleonReader("158", steam = True)
SpecificItemRepo.initialise(idleonReader.codeReader)
# ItemRepo.initialise(idleonReader.codeReader)
