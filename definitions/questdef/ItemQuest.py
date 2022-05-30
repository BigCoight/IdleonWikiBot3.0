from typing import List

from definitions.component.ComponentBase import ComponentBase
from definitions.questdef.Quest import Quest


class ItemQuest(Quest):
	ItemReq: List[ComponentBase]

	def getRequirements(self) -> List[ComponentBase]:
		return self.ItemReq
