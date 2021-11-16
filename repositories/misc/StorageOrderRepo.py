from typing import List

from definitions.misc.StorageOrders import StorageOrder
from helpers.HelperFunctions import getFrom4dArray
from repositories.master.Repository import Repository


class StorageOrderRepo(Repository[StorageOrder]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["StorageOrder"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFrom4dArray(cls.getSection())[0]
		# Fixing the data as it is stored both as a list of lists and a split array
		ind = 0
		for i, v in enumerate(data[1]):
			if len(v) > 3:
				ind = i
				break
		invBags = data[0]
		storageChest = data[1][:ind]
		maxCaps = data[1][ind:]

		for bag in invBags:
			cls.add(bag[2], StorageOrder(
				order = bag[0],
				obtainable = bag[1] == "1",
				bag = bag[2])
			        )

		for storage in storageChest:
			cls.add(storage[2], StorageOrder(
				order = storage[0],
				obtainable = storage[1] == "1",
				bag = storage[2])
			        )
