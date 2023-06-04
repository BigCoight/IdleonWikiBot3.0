# newV = IdleonReader("1561", True)
# oldV = IdleonReader("156", True)
# NpcRepo.initialise(newV.codeReader)
from helpers.CodeReader import IdleonReader
from repositories.item.RecipeRepo import RecipeRepo

newV = IdleonReader("184", True)

RecipeRepo.initialise(newV.codeReader)
RecipeRepo.upload(False)
