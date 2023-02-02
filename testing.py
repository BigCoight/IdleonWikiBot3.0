# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.talents.ActiveTalentRepo import ActiveTalentRepo

newV = IdleonReader("174", True)
oldV = IdleonReader("173", True)

ActiveTalentRepo.compareVersions(oldV, newV)
