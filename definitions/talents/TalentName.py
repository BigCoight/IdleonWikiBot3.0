from pydantic import BaseModel

from helpers.CustomTypes import Integer


class TalentName(BaseModel):
	name: str
	id: Integer
