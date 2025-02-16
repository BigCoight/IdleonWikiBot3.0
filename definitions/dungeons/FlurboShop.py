from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class FlurboShop(IdleonModel):
	intId: str
	cost: Integer
	noPurchases: Integer
	displayName: str
	description: str

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		item = ItemDetailRepo.getDisplayName(self.intId)
		craftRec = "{{ItemDisplay|" + item + "}}"
		return f"|{craftRec} || {self.description} || {self.cost} || {self.noPurchases}\n|-"
