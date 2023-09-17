# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.weeklyboss.WeeklyBossRepo import WeeklyBossRepo

newV = IdleonReader("191", True)

WeeklyBossRepo.initialise(newV.codeReader)
