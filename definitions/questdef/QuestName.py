from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel


class QuestName(IdleonModel):
	name: str
	difficulty: int
