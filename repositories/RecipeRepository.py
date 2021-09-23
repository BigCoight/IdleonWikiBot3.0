
from typing import Dict, Type, Union

from definitions.itemdef.Recipe import Recipe, Component
from repositories.Repository import Repository
from definitions.itemdef.itemtypes.CommonItem import CommonItem
from definitions.itemdef.itemtypes.QuestItem import QuestItem
from definitions.itemdef.itemtypes.EquipItem import EquipItem
from definitions.itemdef.itemtypes.ConsumableItem import ConsumeableItem
from helpers.HelperFunctions import formatStr, scientificToInt
import re


class RecipeRepository(Repository[Recipe]):

    @ classmethod
    def generateRepo(cls) -> None:
        def wrap(v: str) -> str:
            return f"[[{v}]]"
        reItems = r'"([a-zA-Z0-_ ]*)"\.'
        anvItemNameData = cls.getSection(0)
        anvItemNames = [x.split(" ") for x in re.findall(reItems, anvItemNameData)]
        recipeData = formatStr(cls.getSection(1), ["\n", "  "])
        recipeSections = [wrap(x) for x in re.split(r"],?],?],\[\[\[", recipeData)]
        levelData = formatStr(cls.getSection(2), ["\n", "  "])
        levelSections = [wrap(x) for x in re.split(r"],?],\[\[", levelData)]
        for i, (recipeSection, levelSection) in enumerate(zip(recipeSections, levelSections)):
            if i >= len(anvItemNames):
                break
            recipeItems = [wrap(x) for x in re.split(r"],?],\[\[", recipeSection)]
            levelItems = [wrap(x) for x in re.split(r"],\[", levelSection)]
            for j, (item, level) in enumerate(zip(recipeItems, levelItems)):
                recipe = re.findall(r'\["([a-zA-Z0-9_]*)", "([0-9]*)"', item)
                recipe = [Component(item =q, quantity = v) for q, v in recipe]
                lvlData = re.findall(r'\["([0-9]*)", "([0-9]*)"', level)
                temp = Recipe(
                    recipe = recipe,
                    levelReqToCraft = lvlData[0][0],
                    expGiven = lvlData[0][1],
                    no = j + 1,
                    tab = i + 1
                )
                cls.add(anvItemNames[i][j], temp)
