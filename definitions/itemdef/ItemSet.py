from definitions.master.IdleonModel import IdleonModel


class ItemSet(IdleonModel):
	set: str

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return f"|setname = {self.set}\n"
