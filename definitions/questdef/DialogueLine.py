from definitions.master.IdleonModel import IdleonModel
from definitions.questdef.QuestType import QuestType
from helpers.CustomTypes import Integer


class DialogueLine(IdleonModel):
	Type: QuestType
	DialogueText: str
	NextIndex: Integer
