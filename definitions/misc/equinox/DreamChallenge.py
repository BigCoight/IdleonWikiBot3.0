from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class DreamChallenge(IdleonModel):
	challenge: str
	req: Integer
	reward: str
	filler: str
