# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.RandoListRepo import RandoListRepo

idleonReader = IdleonReader("158", steam = True)
RandoListRepo.initialise(idleonReader.codeReader)
# ItemRepo.initialise(idleonReader.codeReader)
