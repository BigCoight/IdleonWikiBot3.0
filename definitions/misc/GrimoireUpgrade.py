from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class GrimoireUpgrade(IdleonModel):
    name: str
    base_cost: Integer  # Index 1 - Cost to purchase the first level
    scaling_factor: Numeric  # Index 2 - How much the cost increases per level
    x1: Integer  # Index 3 - Unknown purpose
    max_level: Integer  # Index 4 - Maximum level of the upgrade
    value: Integer  # Index 5 - Base value used in bonus calculations
    unlock_req: Integer  # Index 6 - Required total Grimoire upgrades to unlock
    x2: Integer  # Index 8 - Unknown purpose
    description: str  # Index 9 - Description of the upgrade
    has_tooltip: bool  # Based on the presence of 製 character and (Tap for Info) text
    tooltip_text: Optional[str]  # Additional tooltip text shown in the UI 