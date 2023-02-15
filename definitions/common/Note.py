from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.Constants import Constants


class Note(IdleonModel):
	note: str

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return "|notes=" + self.note.replace(Constants.newLineRep, "\n") + "\n"

	@validator("note")
	def validateNote(cls, v: str) -> str:
		return v.replace("}}\n", "").replace('"', "'")
