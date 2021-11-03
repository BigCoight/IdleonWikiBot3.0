from typing import List, Union

from pydantic import validator

from definitions.common.Component import Component
from definitions.common.CustomReq import CustomReq
from definitions.common.ExpType import ExpType
from definitions.master.IdleonModel import IdleonModel
from definitions.questdef.DialogueLine import DialogueLine
from helpers.CustomTypes import Integer


class CoinReward(IdleonModel):
	coins: Integer

	def shouldCompare(self) -> bool:
		return False

	def __str__(self):
		return "{{Coindisplay|" + str(self.coins) + "}}"


class ExpReward(IdleonModel):
	type: ExpType
	amount: Integer

	def shouldCompare(self) -> bool:
		return False

	def __str__(self):
		return f"{self.amount}x {self.type.name} Experience"


class Quest(DialogueLine):
	ConsumeItems: bool
	InventorySpacesNeeded: Integer
	NoSpaceIndex: Integer
	Rewards: List[Union[ExpReward, CoinReward, Component]]
	QuestName: str
	Difficulty: Integer = 0

	@validator("ConsumeItems", pre = True)
	def convertStrBool(cls, v: str) -> bool:
		if v == "!0":
			return True
		return False

	def getRequirements(self) -> Union[List[Component], List[CustomReq]]:
		raise NotImplementedError

	def writeWiki(self, newLine = True) -> str:
		res = "{{Quest"
		res += f"|name={self.Name}\n"
		res += f"|text={self.DialogueText}\n"
		res += f"|difficulty={self.Difficulty}\n"
		res += f"|requirements={', '.join(map(lambda x: str(x), self.getRequirements()))}\n"
		res += f"|consumed={'Yes' if self.ConsumeItems else 'No'}\n"
		res += f"|rewards={', '.join(map(lambda x: str(x), self.Rewards))}\n"
		res += "}}\n"
		return res
