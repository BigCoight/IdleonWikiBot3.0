# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world5.ArtifactRepo import ArtifactRepo

newV = IdleonReader("180", True)

ArtifactRepo.initialise(newV.codeReader)
