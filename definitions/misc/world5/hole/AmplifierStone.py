from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class AmplifierStone(IdleonModel):
	name: str
	desc: str
	perLvl: Numeric
	maxVal: Numeric
