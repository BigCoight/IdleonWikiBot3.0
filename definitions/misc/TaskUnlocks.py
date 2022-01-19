from typing import List

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel


class TaskUnlock(IdleonModel):
	item: str
	tabNo: int
	recipNo: int


class TaskUnlocks(IdleonModel):
	unlocks: List[List[TaskUnlock]]


