from typing import Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel


class CollectionModel(IdleonModel):

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {}

	def wikiWriterKey(self):
		raise NotImplementedError
