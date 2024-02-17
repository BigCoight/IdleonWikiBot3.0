# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world6.NinjaItemRepo import NinjaItemRepo

newV = IdleonReader("200", True)

NinjaItemRepo.initialise(newV.codeReader)
