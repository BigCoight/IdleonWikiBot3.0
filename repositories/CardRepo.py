
import re
from typing import List

from definitions.itemdef.CardData import CardData
from helpers.HelperFunctions import formatStr, wrap, strToArray
from repositories.Repository import Repository


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
