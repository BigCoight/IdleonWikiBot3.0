from pydantic import BaseModel


class TalentName(BaseModel):
	name: str
	id: int
