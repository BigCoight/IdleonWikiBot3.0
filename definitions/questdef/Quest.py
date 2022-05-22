from typing import List, Union

from pydantic import validator

from definitions.common.Component import Component
from definitions.common.CustomReq import CustomReq
from definitions.common.ExpType import ExpType
from definitions.common.Note import Note
from definitions.questdef.DialogueLine import DialogueLine
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.talents.TalentNameRepo import TalentNameRepo


class CoinReward(Component):

	def __str__(self):
		return "{{Coindisplay|" + str(self.quantity) + "}}"


class ExpReward(Component):
	def __str__(self):
		typ = ExpType(int(self.item[10:]))
		return f"{self.quantity} {typ.name} Experience"


class RecipeReward(Component):
	def __str__(self):
		tab = int(self.item[-1]) - 1
		index = int(self.quantity) + 1
		item = ItemDetailRepo.getDisplayName(RecipeRepo.getItemAtIndex(tab, index))
		return f"{item} Recipe"


class TalentReward(Component):
	def __str__(self):
		qty = str(self.quantity)
		no = int(qty[0])
		index = int(qty[1: no + 1])
		talent = TalentNameRepo.getList(index).name
		return f"{talent} Talent Book"


class Quest(DialogueLine):
	ConsumeItems: bool
	InventorySpacesNeeded: Integer
	NoSpaceIndex: Integer
	Rewards: List[Component]
	QuestName: str
	Difficulty: Integer = 0
	note: Note = Note(note = " ")

	@validator("ConsumeItems", pre = True)
	def convertStrBool(cls, v: str) -> bool:
		if v == "!0":
			return True
		return False

	def getRequirements(self) -> Union[List[Component], List[CustomReq]]:
		raise NotImplementedError

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		questText = self.DialogueText.split("QUEST:")
		q = self.DialogueText
		if len(questText) > 1:
			q = questText[1]
		res = "{{Quest"
		res += f"|name={self.Name}\n"
		res += f"|text={q}\n"
		res += f"|difficulty={self.Difficulty}\n"
		res += f"|requirements={', '.join(map(lambda x: str(x), self.getRequirements()))}\n"
		res += f"|consumed={'Yes' if self.ConsumeItems else 'No'}\n"
		res += f"|rewards={', '.join(map(lambda x: str(x), self.Rewards))}\n"
		res += f"|notes={self.note.note}\n"
		res += "}}\n"
		return res
