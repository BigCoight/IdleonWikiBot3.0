from typing import List

from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class Part(BaseModel):
	item: str
	base: int
	increment: Numeric


class PostOffice(BaseModel):
	orders: List[Part]
	coinRewards: List[int]
	rewards: List[Part]
