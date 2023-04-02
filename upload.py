from pywikibot.data.api import LoginManager

from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.collections.ItemRepo import ItemRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.npc.NpcRepo import NpcRepo

loginManager = LoginManager()
loginManager.login()

newV = IdleonReader("179", True)
oldV = IdleonReader("178", True)
upload = True

# ItemRepo.initialise(oldV.codeReader, log = False)
# EnemyRepo.initialise(oldV.codeReader, log = False)
# NpcRepo.initialise(oldV.codeReader, log = False)
# DropTableRepo.initialise(oldV.codeReader, log = False)
#
# ItemRepo._manualOld()
# EnemyRepo._manualOld()
# NpcRepo._manualOld()
# DropTableRepo._manualOld()

ItemRepo.initialise(newV.codeReader, log = False)
EnemyRepo.initialise(newV.codeReader, log = False)
NpcRepo.initialise(newV.codeReader, log = False)
DropTableRepo.initialise(newV.codeReader, log = False)

ItemRepo.upload(not upload)
EnemyRepo.upload(not upload)
NpcRepo.upload(not upload)
DropTableRepo.upload(not upload)
