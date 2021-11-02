from definitions.master.IdleonModel import IdleonModel
from definitions.questdef.QuestType import QuestType
from helpers.CustomTypes import Integer


class DialogueLine(IdleonModel):
	Type: QuestType
	DialogueText: str
	NextIndex: Integer

	def writeWiki(self, newLine = True) -> str:
		return "{{dialogue/row|text=" + self.DialogueText + "}}\n"
