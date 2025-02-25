from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class UpgradeVault(IdleonModel):
    name: str
    base_cost: Integer
    scaling_factor: Numeric
    x1: Integer  # Unknown purpose, was previously 'position'
    unlock_req: Integer  # Field at index 4
    value: Integer
    max_level: Integer
    description_line1: str  # First line of description
    description_line2: Optional[str]  # Second line of description (optional)
    has_tooltip: bool  # Based on the presence of 製 character and (Tap for Info) text
    x2: Optional[str]  # Unknown purpose, was previously 'effect_type'
    tooltip_text: Optional[str]  # Additional tooltip text shown in the UI 