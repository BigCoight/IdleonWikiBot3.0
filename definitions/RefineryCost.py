from typing import List

from pydantic import BaseModel

from definitions.common.Component import Component


class RefineryCost(BaseModel):
	cost: List[Component]
