# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.weeklyboss.WeeklyShopRepo import WeeklyShopRepo

newV = IdleonReader("192", True)

WeeklyShopRepo.initialise(newV.codeReader)
