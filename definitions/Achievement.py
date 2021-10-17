from pydantic import BaseModel

from helpers.CustomTypes import Integer


class Achievement(BaseModel):
	name: str
	qty: Integer
	desc: str
	rewards: str

