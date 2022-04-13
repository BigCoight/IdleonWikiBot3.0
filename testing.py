from helpers.CodeReader import IdleonReader
from repositories.collections.ItemRepo import ItemRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyTableRepo import EnemyTableRepo
from repositories.item.CardDropChanceRepo import CardDropChanceRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.TrapBoxRepo import TrapBoxRepo
from repositories.misc.CardSetRepo import CardSetRepo
from repositories.misc.ColosseumRepo import ColosseumRepo
from repositories.misc.RandoListRepo import RandoListRepo

newV = IdleonReader("153", True)

oldV = IdleonReader("152", True)
RandoListRepo.initialise(newV.codeReader)
