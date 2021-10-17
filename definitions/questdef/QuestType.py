from enum import Enum

from definitions.common.EnumMeta import CheckIn


class QuestType(str, Enum, metaclass=CheckIn):
	NoQuest = "None"
	Custom = "Custom"
	ItemsAndSpaceRequired = "ItemsAndSpaceRequired"
	LevelReq = "LevelReq"
	SpaceRequired = "SpaceRequired"
