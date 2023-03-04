# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.talents.TalentTreeRepo import TalentTreeRepo

newV = IdleonReader("177", True)
oldV = IdleonReader("176", True)

TalentTreeRepo.compareVersions(oldV, newV)
