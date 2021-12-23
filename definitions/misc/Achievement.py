from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class Achievement(IdleonModel):
	name: str
	qty: Integer
	desc: str
	rewards: str

