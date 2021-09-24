
from typing import Dict, Type, Union, List

from definitions.itemdef.CardData import CardData
from definitions.itemdef.Recipe import Recipe, Component
from repositories.Repository import Repository
from definitions.itemdef.itemtypes.CommonItem import CommonItem
from definitions.itemdef.itemtypes.QuestItem import QuestItem
from definitions.itemdef.itemtypes.EquipItem import EquipItem
from definitions.itemdef.itemtypes.ConsumableItem import ConsumeableItem
from helpers.HelperFunctions import formatStr, scientificToInt, wrap, strToArray
import re


class CardRepo(Repository[CardData]):

    @classmethod
    def getSections(cls) -> List[str]:
        return ["CardInfo"]

    @ classmethod
    def generateRepo(cls) -> None:
        cardNames = ["Blunder Hills", "Yum Yum Desert", "Easy Resources",
                     "Medium Resources", "Frostbite Tundra", "Hard Resources", "Bosses", "Event"]
        cardData = formatStr(cls.getSection(), ["\n", "  "])
        for n, section in enumerate([wrap(x) for x in re.split(r",?],?],\[\[", cardData)]):
            for m, data in enumerate([wrap(x) for x in re.split(r",?],\[", section)]):
                arrayData = strToArray(data)
                temp = CardData(
                    cardID = arrayData[1],
                    category = cardNames[n],
                    perTier = arrayData[2],
                    effect = arrayData[3],
                    bonus = arrayData[4],
                    order = m + 1,
                )
                cls.add(arrayData[0], temp)
