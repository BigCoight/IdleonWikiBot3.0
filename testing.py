from helpers.CodeReader import IdleonReader
from repositories.collections.ItemRepo import ItemRepo
from repositories.item.CardDropChanceRepo import CardDropChanceRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.TrapBoxRepo import TrapBoxRepo
from repositories.misc.CardSetRepo import CardSetRepo

newV = IdleonReader("152", True)

oldV = IdleonReader("140", True)
TrapBoxRepo.compareVersions(oldV, newV)
