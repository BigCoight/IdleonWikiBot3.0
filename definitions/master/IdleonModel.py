from __future__ import annotations

from typing import List, Dict, Union, Callable, Set

from pydantic import BaseModel


class IdleonModel(BaseModel):
	@classmethod
	def fromList(cls, data: List[any]) -> IdleonModel:
		keys = cls.__fields__.keys()
		if len(keys) != len(data):
			raise ValueError(f"Length of keys ({len(keys)}) does not match length of data ({len(data)})")
		return cls.parse_obj({key: val for key, val in zip(keys, data)})

	def shouldCompare(self) -> bool:
		return True

	def writeWiki(self, newLine = True) -> str:
		res = ""
		for wiki, atr in self.intToWiki().items():
			if isinstance(atr, str):
				if self.dict()[atr] and self.dict()[atr] not in {"00"}:
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
		firstIter = dict(self)
		for atr, val in firstIter.items():
			if isinstance(val, IdleonModel) and val.shouldCompare():
				firstIter[atr] = val.toDict(ignored)
			if isinstance(val, list):
				if not val:
					continue
				elif isinstance(val[0], IdleonModel) and val[0].shouldCompare():
					firstIter[atr] = [x.toDict(ignored) for x in val]
			if isinstance(val, dict):
				key = list(val.keys())[0]
				if isinstance(val[key], IdleonModel) and val[key].shouldCompare():
					firstIter[atr] = {k: v.toDict(ignored) for k, v in val.items()}

		for ignore in ignored:
			firstIter.pop(ignore, None)
		return firstIter

	def compare(self, other: IdleonModel, ignored: Set[str] = set()):
		diffs = {}
		d1 = dict(self)
		d2 = dict(other)
		keys = d1.keys()
		for key in keys:
			if d1[key] == d2[key]:
				continue
			if key in ignored:
				continue
			if isinstance(d1[key], IdleonModel) and d1[key].shouldCompare():
				diffs[key] = d1[key].compare(d2[key], ignored)
				continue
			if isinstance(d1[key], list):
				diffs[key] = self._getDifList(d1[key], d2[key], ignored)
				continue
			if isinstance(d1[key], dict):
				diffs[key] = self._getDifDict(d1[key], d2[key], ignored)
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
				toAdd = other[key].toDict()
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
