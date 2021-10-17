from typing import List

from pydantic import BaseModel

from helpers.CustomTypes import Numeric, Integer


class Part(BaseModel):
	item: str
	base: Integer
	increment: Numeric


class PostOffice(BaseModel):
	orders: List[Part]
	coinRewards: List[Integer]
	rewards: List[Part]
