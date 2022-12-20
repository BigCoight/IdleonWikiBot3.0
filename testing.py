# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world5.ArtifactRepo import ArtifactRepo
from repositories.misc.world5.CaptainBonusRepo import CaptainBonusRepo
from repositories.misc.world5.DivinityStyleRepo import DivinityStyleRepo
from repositories.misc.world5.GamingBoxRepo import GamingBoxRepo
from repositories.misc.world5.GamingUpgradeRepo import GamingUpgradeRepo
from repositories.misc.world5.GodInfoRepo import GodInfoRepo
from repositories.misc.world5.IslandInfoRepo import IslandInfoRepo

idleonReader = IdleonReader("170", steam = True).codeReader

ArtifactRepo.initialise(idleonReader)
CaptainBonusRepo.initialise(idleonReader)
DivinityStyleRepo.initialise(idleonReader)
GamingBoxRepo.initialise(idleonReader)
GamingUpgradeRepo.initialise(idleonReader)
GodInfoRepo.initialise(idleonReader)
IslandInfoRepo.initialise(idleonReader)
