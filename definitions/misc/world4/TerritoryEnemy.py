from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class TerritoryEnemy(IdleonModel):
    id: str
    health: Numeric
    colour: Numeric
    size: Numeric
