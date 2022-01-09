from definitions.master.IdleonModel import IdleonModel
from definitions.questdef.QuestType import QuestType
from helpers.CustomTypes import Integer


class DialogueLine(IdleonModel):
	Type: QuestType
	DialogueText: str
	NextIndex: Integer
	Name: str = ""

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{dialogue/row|text=" + self.DialogueText
		if self.Name:
			res += f"|quest={self.Name}"
		return res + "}}\n"
