from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class CustomReq(IdleonModel):
	desc: str
	finalV: Integer
	type: str
	startV: Integer

	def shouldCompare(self) -> bool:
		return False

	def __str__(self) -> str:
		return f"{self.desc} > {self.finalV}"
