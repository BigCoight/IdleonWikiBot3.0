from pywikibot.data.api import LoginManager

from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.collections.ItemRepo import ItemRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.npc.NpcRepo import NpcRepo

loginManager = LoginManager()
loginManager.login()

newV = IdleonReader("160", True)
oldV = IdleonReader("157", True)
upload = True

ItemRepo.initialise(newV.codeReader, log = False)
EnemyRepo.initialise(newV.codeReader, log = False)
NpcRepo.initialise(newV.codeReader, log = False)
DropTableRepo.initialise(newV.codeReader, log = False)

ItemRepo.upload(not upload)
EnemyRepo.upload(not upload)
NpcRepo.upload(not upload)
DropTableRepo.upload(not upload)
