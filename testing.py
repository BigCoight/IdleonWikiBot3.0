# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.item.UsesRepo import UsesRepo

newV = IdleonReader("174", True)

UsesRepo.initialise(newV.codeReader)
