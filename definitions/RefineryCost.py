from typing import List

from definitions.common.Component import Component
from definitions.master.IdleonModel import IdleonModel


class RefineryCost(IdleonModel):
	cost: List[Component]
