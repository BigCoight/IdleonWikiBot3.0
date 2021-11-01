from definitions.master.IdleonModel import IdleonModel


class Note(IdleonModel):
	note: str

	def writeWiki(self, newLine = True) -> str:
		return "|notes=" + self.note + "\n"
