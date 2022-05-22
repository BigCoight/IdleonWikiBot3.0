# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.talents.TalentTreeRepo import TalentTreeRepo

idleonReader = IdleonReader("157alphab", steam = True)
TalentTreeRepo.initialise(idleonReader.codeReader)
