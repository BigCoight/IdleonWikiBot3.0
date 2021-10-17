from pydantic import BaseModel


class QuestName(BaseModel):
	name: str
	difficulty: int
