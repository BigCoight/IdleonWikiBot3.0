from typing import List

from pydantic import BaseModel


class TaskUnlock(BaseModel):
	item: str
	tabNo: int
	recipNo: int


class TaskUnlocks(BaseModel):
	unlocks: List[List[TaskUnlock]]


