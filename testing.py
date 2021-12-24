from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.collections.ItemRepo import ItemRepo
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.talents.ActiveTalentRepo import ActiveTalentRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

idleonReader = IdleonReader("140b", True)
# idleonReader = IdleonReader("123b", False)
codeReader = idleonReader.codeReader

ActiveTalentRepo.initialise(codeReader)