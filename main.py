from repositories.ItemRepository import ItemRepository
from helpers.CodeReader import CodeReader

codeReader = CodeReader("idleon123b.txt")
codeReader.addSection('__name__ = "scripts.ItemDefinitions";',
                      "addNewItem = function", "Items")
codeReader.readCode()

ItemRepository.initialise(codeReader, "Items")

print(ItemRepository.get("GemQ7"))
