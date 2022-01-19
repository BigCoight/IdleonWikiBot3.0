from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel


class DungTrait(IdleonModel):
	name: str
