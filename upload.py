from pywikibot.data.api import LoginManager

from helpers.CodeReader import IdleonReader
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.collections.ItemRepo import ItemRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.npc.NpcRepo import NpcRepo

loginManager = LoginManager()
loginManager.login()

newV = IdleonReader("1561", True)
oldV = IdleonReader("156", True)
upload = True

ItemRepo.initialise(newV.codeReader)
EnemyRepo.initialise(newV.codeReader)
NpcRepo.initialise(newV.codeReader)
DropTableRepo.initialise(newV.codeReader)

ItemRepo.upload(not upload)
EnemyRepo.upload(not upload)
NpcRepo.upload(not upload)
DropTableRepo.upload(not upload)
