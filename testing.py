# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.collections.ItemRepo import ItemRepo

newV = IdleonReader("187", True)

ItemRepo.initialise(newV.codeReader)
