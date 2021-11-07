from pydantic import validator

from definitions.master.IdleonModel import IdleonModel


class Note(IdleonModel):
	note: str

	def writeWiki(self, newLine = True) -> str:
		return "|notes=" + self.note + "\n"

	@validator("note")
	def validateNote(cls, v: str) -> str:
		return v.replace("}}\n", "").replace('"', "'")
