from __future__ import annotations

from typing import List, Dict, Union, Callable

from pydantic import BaseModel


class IdleonModel(BaseModel):

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

		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {}

	def writeAfter(self) -> List[IdleonModel]:
		return []

	def compare(self, other: IdleonModel):
		diffs = {}
		d1 = dict(self)
		d2 = dict(other)
		keys = d1.keys()
		for key in keys:
			if d1[key] == d2[key]:
				continue
			if isinstance(d1[key], BaseModel):
				diffs[key] = d1[key].compare(d2[key])
				continue
			if isinstance(d1[key], List):
				diffs[key] = self._getDifList(d1[key], d2[key])
				continue
			diffs[key] = (d1[key], d2[key])
		return diffs

	def _getDifList(self, me, other) -> List[any]:
		res = []
		len1 = len(me)
		len2 = len(other)

		if len1 < len2:
			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel):
					res.append(me[i].compare(other[i]))
					continue
				res.append((me[i], other[i]))
			for i in other[len1:len2]:
				res.append(("", i))

		else:
			for i in range(len2):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel):
					res.append(me[i].compare(other[i]))
					continue
				res.append((me[i], other[i]))
			for i in other[len2:len1]:
				res.append((i, ""))

		return res
