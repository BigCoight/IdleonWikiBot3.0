from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class StorageOrder(IdleonModel):
	order: Integer
	obtainable: bool
	bag: str


class StorageOrders(IdleonModel):
	order: List[StorageOrder]
