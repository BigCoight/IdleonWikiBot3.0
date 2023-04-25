from typing import List

from definitions.master.IdleonModel import IdleonModel


class RandoList(IdleonModel):
	elements: List[str]

	def __getitem__(self, item):
		return self.elements[item]
