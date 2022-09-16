# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.MapNameRepo import MapNameRepo

idleonReader = IdleonReader("-is", steam = True)
MapNameRepo.initialise(idleonReader.codeReader)
# ItemRepo.initialise(idleonReader.codeReader)
