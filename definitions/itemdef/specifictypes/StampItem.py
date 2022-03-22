from __future__ import annotations

from typing import Tuple, Dict, Union, Callable, List

from definitions.common.QtylessComponent import QtylessComponent
from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.BonusItem import BonusItem
from definitions.master.IdleonModel import IdleonModel
from helpers.Constants import Constants
from helpers.CustomTypes import Numeric, Integer
from helpers.HelperFunctions import replaceUnderscores, formatStr
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.StampDescriptionRepo import StampDescriptionRepo


class StampData(IdleonModel):
	effect: str
	function: str
	x1: Numeric
	x2: Numeric
	upgradeInterval: Numeric
	material: QtylessComponent
	startV: Numeric
	mCostExp: Numeric
	startingCost: Numeric
	cCostExp: Numeric
	i10: Numeric
	upgradeText: str
	i12: Numeric

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{stampdata"
		res += super().writeWiki(newLine = False, ignoreZero = False)
		res += "}}\n"
		return res

	def getMaterial(self):
		if ItemDetailRepo.contains(self.material.item):
			return ItemDetailRepo.getDisplayName(self.material.item)
		return self.material

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"stype": "effect",
			"ftype": "function",
			"x1": "x1",
			"x2": "x2",
			"i4": "upgradeInterval",
			"material": self.getMaterial,
			"i6": "startV",
			"i7": "mCostExp",
			"i8": "startingCost",
			"i9": "cCostExp",
			"i10": "i10",
			"i11": "upgradeText",
			"i12": "i12"
		}


class StampItem(BonusItem):

	@classmethod
	def getBonus(cls, item: Union[ConsumableItem, QuestItem]) -> str:
		if item.displayName == "FILLER":
			return "FILLER"
		s, t = cls.stampType(item)
		descs = StampDescriptionRepo.get(s)
		return descs.descriptions[t-1]

	@classmethod
	def getDesc(cls, item: Union[ConsumableItem, QuestItem]) -> str:
		return ""

	ID: Integer
	stampData: StampData

	@classmethod
	def fromItemDetails(cls, item: QuestItem) -> BaseItem:
		stampData = item.desc_line1.split(",")
		t, i = cls.stampType(item)
		return StampItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = t,
			ID = i,
			bonus = cls.getBonus(item),
			description = cls.getDesc(item),
			stampData = StampData(
				effect = stampData[0],
				function = stampData[1],
				x1 = stampData[2],
				x2 = stampData[3],
				upgradeInterval = stampData[4],
				material = QtylessComponent(item = stampData[5]),
				startV = stampData[6],
				mCostExp = stampData[7],
				startingCost = stampData[8],
				cCostExp = stampData[9],
				i10 = stampData[10],
				upgradeText = replaceUnderscores(stampData[11]),
				i12 = stampData[12]))

	@classmethod
	def stampType(cls, item: QuestItem) -> Tuple[str, int]:
		ind = 0
		id = str(item.ID)
		if len(id) > 2:
			ind = int(id[0])

		return Constants.stampTypes[ind], int(id[-2:]) + 1

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {
			"number": "ID",
			"material": self.getMaterial,
			"bonus": self.getBonusWiki
		}
		return {**base, **extra}

	def getBonusWiki(self) -> str:
		return formatStr(self.bonus, ["{", "}"])

	def writeAfter(self) -> List[IdleonModel]:
		return [self.stampData]

	def getMaterial(self):
		if ItemDetailRepo.contains(self.stampData.material.item):
			return ItemDetailRepo.getDisplayName(self.stampData.material.item)
		return self.stampData.material
