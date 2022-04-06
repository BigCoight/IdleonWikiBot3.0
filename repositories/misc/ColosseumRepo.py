from definitions.misc.Colosseum import Colosseum, ColEnemy, ColWave
from definitions.misc.TaskUnlocks import TaskUnlocks, TaskUnlock
from helpers.Constants import Constants
from helpers.HelperFunctions import getFrom4dArray, getFromArrayArray
from typing import List

from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.Repository import Repository


class ColosseumRepo(Repository[Colosseum]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		EnemyDetailsRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ColInfo", "ColWaves"]

	@classmethod
	def generateRepo(cls) -> None:
		cols = getFrom4dArray(cls.getSection(1))
		info = getFromArrayArray(cls.getSection())

		for n, waves in enumerate(cols):
			colWaves = []
			for wave in waves:
				colWave = []
				for enemy in wave:
					colWave.append(ColEnemy.fromList(enemy))

				colWaves.append(ColWave(enemies=colWave.copy()))
			data = [Constants.COLNAMES[n]] + info[n]
			data.append(colWaves.copy())
			toAdd = Colosseum.fromList(data)
			cls.add(Constants.COLNAMES[n], toAdd)
			cls.addList(toAdd)

