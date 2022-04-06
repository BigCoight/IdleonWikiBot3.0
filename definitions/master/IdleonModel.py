from __future__ import annotations

import difflib
import enum
from collections import Counter
from typing import List, Dict, Union, Callable, Set

from pydantic import BaseModel


class IdleonModel(BaseModel):
	@classmethod
	def fromList(cls, data: List[any]) -> IdleonModel:
		keys = cls.__fields__.keys()
		if len(keys) != len(data):
			raise ValueError(f"Error in creating {cls.__name__}:\n"
			                 f" Length of object keys ({len(keys)}) does not match length of input data "
			                 f"({len(data)})")
		return cls.parse_obj({key: val for key, val in zip(keys, data)})

	def shouldCompare(self) -> bool:
		return True

	def isFiller(self) -> bool:
		return False

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = ""
		for wiki, atr in self.intToWiki().items():
			if isinstance(atr, str):
				cVal = self.dict()[atr]
				if (not cVal or cVal in {"00"}) and ignoreZero:
					continue
				res += f"|{wiki}={self.dict()[atr]}"
				if newLine:
					res += "\n"
			else:
				if atr():
					res += f"|{wiki}={atr()}"
					if newLine:
						res += "\n"
		self.dict()

		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {}

	def writeAfter(self) -> List[IdleonModel]:
		return []

	def toDict(self, ignored: Set[str] = set()) -> Dict[str, any]:
		firstIter = {}
		for atr, val in self:
			if isinstance(val, IdleonModel) and val.shouldCompare():
				subDict = val.toDict(ignored)
				if not subDict:
					firstIter[atr] = subDict
					continue
				if len(subDict.keys()) > 1:
					firstIter[atr] = subDict
					continue
				key = list(subDict.keys())[0]
				firstIter[atr] = subDict[key]
				continue
			if isinstance(val, list) and val:
				if not val:
					continue
				if isinstance(val[0], IdleonModel) and val[0].shouldCompare():
					firstIter[atr] = [x.toDict(ignored) for x in val]
					continue
			if isinstance(val, dict) and val:
				key = list(val.keys())[0]
				if isinstance(val[key], IdleonModel) and val[key].shouldCompare():
					firstIter[atr] = {k: v.toDict(ignored) for k, v in val.items()}
					continue
			if isinstance(val, enum.Enum):
				firstIter[atr] = val.name
				continue
			firstIter[atr] = val

		for ignore in ignored:
			firstIter.pop(ignore, None)
		return firstIter

	def compare(self, other: IdleonModel, ignored: Set[str] = set()):
		diffs = {}
		d1 = self.__dict__
		d2 = other.__dict__
		keys = d1.keys()
		for key in keys:
			if d1[key] == d2[key]:
				continue
			if key in ignored:
				continue
			if isinstance(d1[key], IdleonModel) and d1[key].shouldCompare():
				if len(d1[key].__fields__) > 1:
					diffs[key] = d1[key].compare(d2[key], ignored)
					continue
				firstKey = list(dict(d1[key]).keys())[0]
				if isinstance(dict(d1[key])[firstKey], list):  # Remove the Drop: Drop: [] iteration
					diffs[key] = self._getDifList(dict(d1[key])[firstKey], dict(d2[key])[firstKey], ignored)
					continue
				diffs[key] = d1[key].compare(d2[key], ignored)
				continue
			if isinstance(d1[key], list):
				diffs[key] = self._getDifList(d1[key], d2[key], ignored)
				continue
			if isinstance(d1[key], dict):
				diffs[key] = self._getDifDict(d1[key], d2[key], ignored)
				continue
			if isinstance(d1[key], enum.Enum):
				diffs[key] = (d1[key].name, d2[key].name)
				continue
			diffs[key] = (d1[key], d2[key])
		if not any(diffs.values()):
			return {}
		return diffs

	def _getDifList(self, me, other, ignored: Set[str] = set()) -> List[any]:
		res = []
		len1 = len(me)
		len2 = len(other)

		if len1 == len2:
			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res.append(me[i].compare(other[i], ignored))
					continue
				res.append((me[i], other[i]))
		elif len1 < len2:

			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res.append(me[i].compare(other[i], ignored))
					continue
				res.append((me[i], other[i]))
			for i in other[len1:len2]:
				res.append((" ", i))
		else:
			for i in range(len2):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res.append(me[i].compare(other[i], ignored))
					continue
				res.append((me[i], other[i]))
			for i in other[len2:len1]:
				res.append((i, " "))

		return res

	def _getDifDict(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		diffs = {}
		keys1 = set(me.keys())
		keys2 = set(other.keys())
		sameItems = keys1.intersection(keys2)
		newItems = keys2 - keys1
		for key in sameItems:
			if me[key] == other[key]:
				continue
			if key in ignored:
				continue
			if isinstance(me[key], IdleonModel) and me[key].shouldCompare():
				diffs[key] = me[key].compare(other[key], ignored)
				continue
			if isinstance(me[key], list):
				diffs[key] = self._getDifList(me[key], other[key], ignored)
				continue
			if isinstance(me[key], dict):
				diffs[key] = self._getDifDict(me[key], other[key], ignored)
				continue
			diffs[key] = (me[key], other[key])

		for key in newItems:
			if isinstance(other[key], IdleonModel) and other[key].shouldCompare():
				toAdd = other[key].toDict(ignored)
				diffs[key] = {}
				for atr, val in toAdd.items():
					if isinstance(val, list):
						diffs[key][atr] = []
						for elem in val:
							diffs[key][atr].append((" ", elem))
						continue
					diffs[key][atr] = (" ", val)
				continue
			diffs[key] = (" ", other[key])
		return diffs
