# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.MapPortalsRepo import MapPortalsRepo

newV = IdleonReader("203", True)
oldV = IdleonReader("201", True)

MapPortalsRepo.initialise(newV.codeReader)
