from typing import Dict, Union, Callable

from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import replaceUnderscores


class FishingToolkit(IdleonModel):
	name: str
	depth1: Integer
	depth2: Integer
	depth3: Integer
	depth4: Integer
	fishingExp: Integer
	fishingSpeed: Integer
	fishingPower: Integer

	_replaceUnderscores = validator("name", allow_reuse = True)(replaceUnderscores)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"depth1": "depth1",
			"depth2": "depth2",
			"depth3": "depth3",
			"depth4": "depth4",
			"fishingexp": "fishingExp",
			"fishingspeed": "fishingSpeed",
			"fishingpower": "fishingPower"
		}
