# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.GemShopRepo import GemShopRepo

newV = IdleonReader("175b", True)

GemShopRepo.initialise(newV.codeReader)
