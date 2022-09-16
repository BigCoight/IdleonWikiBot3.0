from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.StatItem import StatItem
from repositories.dungeons.KeychainBonusRepo import KeychainBonusRepo


class KeychainItem(StatItem):

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
		return KeychainItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			lvReqToCraft = item.lvReqToCraft,
			lvReqToEquip = item.lvReqToEquip,
			Class = item.Class,
			Weapon_Power = item.Weapon_Power,
			STR = item.STR,
			AGI = item.AGI,
			WIS = item.WIS,
			LUK = item.LUK,
			Defence = item.Defence,
			miscUp1 = cls.getMisc1(item),
			miscUp2 = cls.getMisc2(item),
			Upgrade_Slots_Left = item.Upgrade_Slots_Left,
		)

	@classmethod
	def getMisc1(cls, item: EquipItem) -> str:
		bonuses = KeychainBonusRepo.get(item.internalID)
		if not bonuses:
			return ""
		return bonuses.writeMisc()

	@classmethod
	def getMisc2(cls, item: EquipItem):
		return "[[Keychains#Misc 2 Rolling|Misc 2 Table]]"
