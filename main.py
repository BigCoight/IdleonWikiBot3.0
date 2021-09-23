from repositories.ItemRepository import ItemRepository
from helpers.CodeReader import CodeReader, IdelonReader
from repositories.RecipeRepository import RecipeRepository

idleonReader = IdelonReader("idleon123b.txt")
codeReader = idleonReader.codeReader

ItemRepository.initialise(codeReader, ["Items"])
RecipeRepository.initialise(codeReader, ["AnvilItems", "Recipes", "RecipeLevel"])

print(RecipeRepository.get("EquipmentShirts30"))
