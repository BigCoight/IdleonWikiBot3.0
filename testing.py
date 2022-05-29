# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.item.ItemDetailRepo import ItemDetailRepo

idleonReader = IdleonReader("157alphab", steam = True)
ItemDetailRepo.initialise(idleonReader.codeReader)
# ItemRepo.initialise(idleonReader.codeReader)
