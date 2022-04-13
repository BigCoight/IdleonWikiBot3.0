from typing import List, Union

from pydantic import validator

from definitions.common.Component import Component
from definitions.common.LiquidComponent import LiquidComponent
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer
from helpers.HelperFunctions import replaceUnderscores


class Sigil(IdleonModel):
	name: str
	unlockCost: Integer
	boostCost: Integer
	unlockBonus: Numeric
	boostBonus: Numeric
	filler: str
	desc: str
