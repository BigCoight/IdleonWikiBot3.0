from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class TalentName(IdleonModel):
	name: str
	id: Integer
