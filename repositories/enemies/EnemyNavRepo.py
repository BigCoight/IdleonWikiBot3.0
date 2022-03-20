from definitions.enemy.EnemyNav import EnemyNav
from helpers.Constants import Constants
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.item.CardRepo import CardRepo
from repositories.master.Repository import Repository
from typing import List


class EnemyNavRepo(Repository[EnemyNav]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		CardRepo.initialise(cls.codeReader, log)

	@classmethod
	def generateRepo(cls) -> None:
		for name, cardData in CardRepo.items():
			if cardData.category not in Constants.navCategories:
				continue
			if not EnemyDetailsRepo.contains(name):
				continue
			cls.add(name, EnemyNav(
				prev = CardRepo.getOrder(cardData.category, cardData.order - 1),
				next = CardRepo.getOrder(cardData.category, cardData.order + 1),
				hasCrystal = not name[:7] == "Crystal",
				crystalName = Constants.worldToCrystal.get(cardData.category),
				hasCard = True,
			))


