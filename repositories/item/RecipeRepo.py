import re
from queue import Queue
from typing import List, Set

from definitions.itemdef.Recipe import Recipe, Component, DetRecipeComponent, DetailedRecipe
from helpers.CodeReader import IdleonReader
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import formatStr, wrap
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class RecipeRepo(Repository[Recipe]):
	"""
	Depends on: ItemDetailRepo, TaskUnlocksRepo, DropTableRepo, EnemyDetailsRepo, EnemyTableRepo
	"""
	anvilItemNames: List[List[str]]

	@classmethod
	def getSections(cls) -> List[str]:
		return ["AnvilItems", "Recipes", "RecipeLevel"]

	@classmethod
	def generateRepo(cls) -> None:
		reItems = r'"([a-zA-Z0-_ ]*)"\.'
		anvItemNameData = cls.getSection(0)
		cls.anvilItemNames = [x.split(" ") for x in re.findall(reItems, anvItemNameData)]
		recipeData = formatStr(cls.getSection(1), ["\n", "  "])
		recipeSections = [wrap(x) for x in re.split(r"],?],?],\[\[\[", recipeData)]
		levelData = formatStr(cls.getSection(2), ["\n", "  "])
		levelSections = [wrap(x) for x in re.split(r"],?],\[\[", levelData)]
		for i, (recipeSection, levelSection) in enumerate(zip(recipeSections, levelSections)):
			if i >= len(cls.anvilItemNames):
				break
			recipeItems = [wrap(x) for x in re.split(r"],?],\[\[", recipeSection)]
			levelItems = [wrap(x) for x in re.split(r"],\[", levelSection)]
			for j, (item, level) in enumerate(zip(recipeItems, levelItems)):
				recipe = re.findall(r'\["([a-zA-Z0-9_]*)", "([0-9]*)"', item)
				recipe = [Component(item = q, quantity = v) for q, v in recipe]
				lvlData = re.findall(r'\["([0-9]*)", "([0-9]*)"', level)
				temp = Recipe(
					intID = cls.anvilItemNames[i][j],
					recipe = recipe,
					levelReqToCraft = lvlData[0][0],
					expGiven = lvlData[0][1],
					no = j + 1,
					tab = i + 1
				)
				cls.add(cls.anvilItemNames[i][j], temp)
		for _, v in cls.items():
			cls.generateDetailedRecipe(v)
			cls.generateDetTotals(v)

	@classmethod
	def getItemAtIndex(cls, tab: int, index: int) -> str:
		return cls.anvilItemNames[tab][index]

	@classmethod
	def getFromComponent(cls, comp: Component) -> str:
		tab = int(comp.item[-1]) - 1
		index = comp.quantity
		return cls.getItemAtIndex(tab, index)

	@classmethod
	def getFromItemStr(cls, item: str, quantity: Integer) -> str:
		tab = int(item[-1]) - 1
		index = quantity
		return cls.getItemAtIndex(tab, index)

	@classmethod
	def generateDetailedRecipe(cls, recipe: Recipe):
		if recipe.detailedRecipe:
			return
		currentRecipe = []
		for component in recipe.recipe:
			currentRecipe.append(DetRecipeComponent(
				indent = 0,
				item = component.item,
				quantity = component.quantity
			))
			cRecipe = cls.get(component.item)
			if cRecipe is None or cRecipe.intID == "FillerMaterial":
				continue
			if cRecipe.detailedRecipe is None:
				cls.generateDetailedRecipe(cRecipe)
			assert cRecipe.detailedRecipe is not None
			for part in cRecipe.detailedRecipe.detRecipe:
				currentRecipe.append(DetRecipeComponent(
					indent = part.indent + 1,
					item = part.item,
					quantity = component.quantity * part.quantity
				))
		recipe.detailedRecipe = DetailedRecipe(detRecipe = currentRecipe)

	@classmethod
	def generateDetTotals(cls, recipe: Recipe):
		total = {}
		queue = Queue()
		for component in recipe.recipe:
			queue.put(component)

		while not queue.empty():
			cComponent = queue.get()
			cRecipe = cls.get(cComponent.item)
			if cRecipe is None or cRecipe.intID == "FillerMaterial":
				total[cComponent.item] = total.get(cComponent.item, 0) + cComponent.quantity
			else:
				for subComponent in cRecipe.recipe:
					queue.put(Component(
						item = subComponent.item,
						quantity = subComponent.quantity * cComponent.quantity
					))

		recipeTotals = [Component(item = i, quantity = q) for i, q in total.items()]
		recipe.detailedRecipe.detRecipeTotals = recipeTotals.copy()
		cls.calculateSellPrice(recipe)

	@classmethod
	def calculateSellPrice(cls, recipe: Recipe):
		sellPrice = 0
		for component in recipe.detailedRecipe.detRecipeTotals:
			sellPrice += ItemDetailRepo.get(component.item).sellPrice * component.quantity
		recipe.sellPrice = sellPrice

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return ItemDetailRepo.getDisplayName(name)

	@classmethod
	def _overrideDict(cls) -> Set[str]:
		return {"recipe"}

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set()):
		return super().compareVersions(v1, v2, {"detailedRecipe", "recipeFrom", 'intID'})
