from typing import List

from pydantic import BaseModel

from definitions.questdef.DialogueLine import DialogueLine
from definitions.questdef.NpcHead import NpcHead
from definitions.questdef.Quest import Quest


class Npc(BaseModel):
	head: NpcHead
	quests: List[Quest]
	dialogue: List[DialogueLine]

