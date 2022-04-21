from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class Achievement(IdleonModel):
	name: str
	qty: Integer
	desc: str
	rewards: str
	world: str

	def sortKey(self) -> str:
		return self.world

	def isFiller(self) -> bool:
		return self.name == "FILLERZZZ ACH"

