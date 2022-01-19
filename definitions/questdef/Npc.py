from typing import List, Dict, Optional

from definitions.master.IdleonModel import IdleonModel
from definitions.questdef.DialogueLine import DialogueLine
from definitions.questdef.NpcHead import NpcHead
from definitions.questdef.Quest import Quest


class Npc(IdleonModel):
	head: Optional[NpcHead]
	quests: Dict[str, Quest]
	dialogue: List[DialogueLine]

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = self.head.writeWiki()
		res += "\n"
		res += "{{Quest/head}}\n"
		for _, quest in self.quests.items():
			res += quest.writeWiki()
		res += "|}\n"
		res += "{{dialogue/head}}\n"
		for dline in self.dialogue:
			res += dline.writeWiki()
		res += "|}"
		return res
