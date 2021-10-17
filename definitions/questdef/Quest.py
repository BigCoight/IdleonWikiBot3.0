from typing import List, Union

from pydantic import BaseModel, validator

from definitions.common.Component import Component
from definitions.common.CustomReq import CustomReq
from definitions.questdef.DialogueLine import DialogueLine
from helpers.CustomTypes import Integer


class Quest(DialogueLine):
	ConsumeItems: bool
	InventorySpacesNeeded: Integer
	NoSpaceIndex: Integer
	Rewards: List[Component]
	QuestName: str
	Difficulty: Integer = 0
	Name: str = ""

	@validator("ConsumeItems", pre = True)
	def convertStrBool(cls, v: str) -> bool:
		if v == "!0":
			return True
		return False

	def getRequirements(self) -> Union[List[Component], List[CustomReq]]:
		raise NotImplementedError

