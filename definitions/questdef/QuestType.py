from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonEnum import IdleonEnum


class QuestType(str, IdleonEnum, metaclass = CheckIn):
	NoQuest = "None"
	Custom = "Custom"
	ItemsAndSpaceRequired = "ItemsAndSpaceRequired"
	LevelReq = "LevelReq"
	SpaceRequired = "SpaceRequired"
