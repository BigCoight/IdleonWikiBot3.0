from typing import List

from definitions.component.ComponentBase import ComponentBase
from definitions.master.IdleonModel import IdleonModel


class RefineryCost(IdleonModel):
	cost: List[ComponentBase]
