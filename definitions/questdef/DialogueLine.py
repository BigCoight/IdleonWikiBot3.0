from pydantic import BaseModel

from definitions.questdef.QuestType import QuestType
from helpers.CustomTypes import Integer


class DialogueLine(BaseModel):
	Type: QuestType
	DialogueText: str
	NextIndex: Integer
