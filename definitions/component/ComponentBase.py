from definitions.master.IdleonModel import IdleonModel


class ComponentBase(IdleonModel):

	def shouldCompare(self) -> bool:
		return False
