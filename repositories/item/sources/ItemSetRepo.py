from definitions.itemdef.ItemSet import ItemSet
from definitions.itemdef.initialtypes.EquipItem import EquipItem
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class ItemSetRepo(Repository[ItemSet]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Item/Sources"

	@classmethod
	def generateRepo(cls) -> None:
		possibleSets = {}
		setPairing = {}
		for item, data in ItemDetailRepo.items():
			if not isinstance(data, (EquipItem)):
				continue
			dispName = data.displayName
			possibleSet = dispName.split(" ")[0]
			setPairing[item] = possibleSet
			if possibleSet not in possibleSets:
				possibleSets[possibleSet] = 0
			possibleSets[possibleSet] += 1

		for intName, possibleSet in setPairing.items():
			count = possibleSets[possibleSet]
			if count >= 4:
				cls.add(intName, ItemSet(set = possibleSet))
