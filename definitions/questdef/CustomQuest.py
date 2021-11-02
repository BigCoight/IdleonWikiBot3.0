from typing import List

from definitions.common.CustomReq import CustomReq
from definitions.questdef.Quest import Quest


class CustomQuest(Quest):
	CustomType: str
	CustomArray: List[CustomReq]

	def getRequirements(self) -> List[CustomReq]:
		return self.CustomArray


