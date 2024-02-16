# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.misc.world6.JadeUpgradeRepo import JadeUpgradeRepo
from repositories.misc.world6.MarketInfoRepo import MarketInfoRepo
from repositories.misc.world6.NinjaItemRepo import NinjaItemRepo
from repositories.misc.world6.NinjaUpgradeRepo import NinjaUpgradeRepo
from repositories.misc.world6.SeedInfoRepo import SeedInfoRepo
from repositories.misc.world6.SummonEnemyRepo import SummonEnemyRepo
from repositories.misc.world6.SummonUnitRepo import SummonUnitRepo
from repositories.misc.world6.SummonUpgradeRepo import SummonUpgradeRepo

newV = IdleonReader("193cb3", True)

SummonUpgradeRepo.initialise(newV.codeReader)
NinjaUpgradeRepo.initialise(newV.codeReader)
JadeUpgradeRepo.initialise(newV.codeReader)
MarketInfoRepo.initialise(newV.codeReader)
SeedInfoRepo.initialise(newV.codeReader)
SummonEnemyRepo.initialise(newV.codeReader)
SummonUnitRepo.initialise(newV.codeReader)
NinjaItemRepo.initialise(newV.codeReader)
