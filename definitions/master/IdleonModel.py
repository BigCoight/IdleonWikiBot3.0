from __future__ import annotations

import enum
import json
import re
from typing import List, Dict, Union, Callable, Set, Any, Optional, Tuple, Type

from pydantic import BaseModel


class ModelConverter:
	class TypeNotFoundError(Exception):
		def __init__(self, typ: str, message: str = "Type was not found in the typeMap object"):
			self.typ = typ
			self.message = message
			super().__init__(f"({typ}) {self.message}")

	def __init__(self, name: str, fields: Dict[str, Any], required: Optional[List[str]], base: IdleonModel,
	             definitions: Optional[Dict[str, Any]]):
		self.needToImport = set()
		self.fields = fields.copy()
		self.name = name + "Model"
		if required:
			self.required = set(required)
		else:
			self.required = set()
		self.base = base
		self.defs = definitions

		self.typeMap = {
			"integer": "number",
			"number": "number",
			"string": "string",
			"boolean": "boolean"
		}

	def toLowerCamel(self, imp: str) -> str:
		return imp[0].lower() + imp[1:]

	def addImport(self, imp: str) -> None:
		self.needToImport.add(imp)

	def extractImports(self) -> str:
		res = []
		for imp in self.needToImport:
			res.append("import { "f"{imp}"" } from "f"'./{self.toLowerCamel(imp)}';")
		return "\n".join(res) + '\n\n'

	def getInnermostType(self, typ: str) -> str:
		if res := self.typeMap.get(typ):
			return res
		raise self.TypeNotFoundError(typ)

	def handleAnyOf(self, anyOf: List[Dict[str, str]]) -> str:
		res = set()
		for typ in anyOf:
			res.add(self.fieldToTs(typ))
		if len(res) == 1:
			return res.pop()
		types = " | ".join(res)
		return f"({types})"

	def handleRef(self, ref: str) -> str:

		split = ref.split("/")
		typ = split[-1]
		if defin := self.defs.get(typ):
			if "enum" in defin:
				self.addImport(typ)
				return typ

		self.addImport(typ + "Model")
		return typ + "Model"

	def getBaseClass(self, cls: str) -> str:
		reGetTypeName = re.compile(r"\.(\w*)(?:$|')")
		return reGetTypeName.findall(cls)[0] + "Model"

	def fieldToTs(self, field: Dict[str, Any]):
		# print(json.dumps(field, indent = 4, sort_keys = True))
		if anyOf := field.get("anyOf"):
			return self.handleAnyOf(anyOf)
		if items := field.get("items"):
			if len(items) > 1 and "type" not in items:
				return self.handleAnyOf(items)
			return self.fieldToTs(items) + "[]"
		if allOf := field.get("allOf"):
			return self.handleAnyOf(allOf)
		if ref := field.get("$ref"):
			return self.handleRef(ref)
		if addProp := field.get("additionalProperties"):
			return f"Record<string, {self.fieldToTs(addProp)}>"
		return self.getInnermostType(field.get("type"))

	def toTS(self):
		# print(json.dumps(self.fields, indent = 4, sort_keys = True))
		res = {}
		# print(self.name)
		for name, field in self.fields.items():
			# print("    " + name)
			res[name] = self.fieldToTs(field)
		base = ""
		if self.base != IdleonModel:
			toRemove = self.base.__fields__.keys()
			for remove in toRemove:
				res.pop(remove)
			base = self.getBaseClass(str(self.base))
			self.addImport(base)
		interface = self.extractImports()
		if not base:
			interface += f"export interface {self.name} ""{\n"
		else:
			interface += f"export interface {self.name} extends {base} ""{\n"
		indent = "    "

		modelFields = []
		for name, typ in res.items():
			required = ""
			if name not in self.required:
				required = "?"
			modelFields.append(f"{indent}{name}{required}: {typ}")
		interface += ",\n".join(modelFields)
		interface += "\n}\n"
		return interface


class IdleonModel(BaseModel):
	@classmethod
	def generateConverter(cls) -> ModelConverter:
		json_schema = json.loads(cls.schema_json())
		# print(json.dumps(json_schema, indent = 4, sort_keys = True))
		properties = json_schema.get("properties")
		required = json_schema.get("required")
		definitions = json_schema.get("definitions")
		base = cls.__bases__[0]
		# print(json.loads(cls.schema_json()))
		exporter = ModelConverter(cls.__name__, properties, required, base, definitions)
		return exporter

	@classmethod
	def toTsInterface(cls):
		return cls.generateConverter().toTS()

	@classmethod
	def getHighestClass(cls) -> Type[IdleonModel]:
		prev = cls
		for parent in cls.mro():
			if parent == IdleonModel:
				return prev
			prev = parent
		return prev

	@classmethod
	def toTsClass(cls, lst: bool) -> str:

		res = f"export class {cls.getHighestClass().__name__}Base"" { "
		dataName = f"{cls.getHighestClass().__name__}Model"
		if lst:
			res += f"constructor(public index: number, public data: {dataName}) ""{ }"
		else:
			res += f"constructor(public id: string, public data: {dataName}) ""{ }"
		return res + " }"

	def toTs(self) -> Tuple[str, Set[str]]:
		converter = TSEncoder(indent = 4)
		res = converter.encode(self)
		return res, converter.needToImport

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

	def compareKey(self) -> str:
		"""

		Returns: in lists of items what key to create compare dicts from
		Examples: eg item name in rewards from quests

		"""
		return ""

	def sortKey(self) -> str:
		"""

		Returns: the element to sort the changelogs by
		Examples:sort items by type, bubbles by cauldron

		"""
		return ""

	def isFiller(self) -> bool:
		"""
		Returns: True if the element was in the code but was filler
		Examples: item name being FILLER

		"""
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

	def _getDifList(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		if isinstance(me[0], IdleonModel) and me[0].compareKey():
			return self._getDifListIdleon(me, other, ignored)
		res = {}
		len1 = len(me)
		len2 = len(other)

		if len1 == len2:
			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
		elif len1 < len2:

			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
			for n, i in enumerate(other[len1:len2]):
				res[str(n)] = (" ", i)
		else:
			for i in range(len2):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
			for n, i in enumerate(other[len2:len1]):
				res[str(n)] = (i, " ")
		if not any(res.values()):
			return {}
		return res

	def _getDifListIdleon(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		meD = {x.compareKey(): {"model": x, "index": str(n)} for n, x in enumerate(me)}
		otherD = {x.compareKey(): {"model": x, "index": str(n)} for n, x in enumerate(other)}

		diffs = {}
		keys1 = set(meD.keys())
		keys2 = set(otherD.keys())
		sameItems = keys1.intersection(keys2)
		newItems = keys2 - keys1
		for key in sameItems:
			if meD[key]["model"] == otherD[key]["model"]:
				continue
			if key in ignored:
				continue
			if isinstance(meD[key]["model"], IdleonModel) and meD[key]["model"].shouldCompare():
				diffs[meD[key]["index"]] = meD[key]["model"].compare(otherD[key]["model"], ignored)
				continue
			if isinstance(meD[key]["model"], list):
				diffs[meD[key]["index"]] = self._getDifList(meD[key]["model"], otherD[key]["model"], ignored)
				continue
			if isinstance(meD[key]["model"], dict):
				diffs[meD[key]["index"]] = self._getDifDict(meD[key]["model"], otherD[key]["model"], ignored)
				continue
			diffs[meD[key]["index"]] = (meD[key]["model"], otherD[key]["model"])

		for key in newItems:
			if isinstance(otherD[key]["model"], IdleonModel) and otherD[key]["model"].shouldCompare():
				toAdd = otherD[key]["model"].toDict(ignored)
				diffs[otherD[key]["index"]] = {}
				for atr, val in toAdd.items():
					if isinstance(val, list):
						diffs[otherD[key]["index"]][atr] = []
						for elem in val:
							diffs[otherD[key]["index"]][atr].append((" ", elem))
						continue
					diffs[otherD[key]["index"]][atr] = (" ", val)
				continue
			diffs[otherD[key]["index"]] = (" ", otherD[key]["model"])

		if not any(diffs.values()):
			return {}
		return diffs

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

		if not any(diffs.values()):
			return {}
		return diffs


class TSEncoder(json.JSONEncoder):
	"""A JSON Encoder that puts small containers on single lines."""

	CONTAINER_TYPES = (list, tuple, dict)
	"""Container datatypes include primitives or other containers."""

	MAX_WIDTH = 90
	"""Maximum width of a container that might be put on a single line."""

	MAX_ITEMS = 5
	"""Maximum number of items in container that might be put on single line."""

	INDENTATION_CHAR = " "

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.base_indent = 12
		self.indentation_level = 0
		self.needToImport = set()

	def encode(self, o):
		"""Encode JSON object *o* with respect to single line lists."""
		if isinstance(o, (list, tuple)):
			if self._put_on_single_line(o):
				return "[" + ", ".join(self.encode(el) for el in o) + "]"
			else:
				self.indentation_level += 1
				output = [self.indent_str + self.encode(el) for el in o]
				self.indentation_level -= 1
				return "[\n" + ",\n".join(output) + "\n" + self.indent_str + "]"
		elif isinstance(o, dict):
			if o:
				output = [f"{json.dumps(k)}: {self.encode(v)}" for k, v in o.items()]
				if self._put_on_single_line(output):
					return "{" + ", ".join(output) + "}"
				self.indentation_level += 1
				output = [self.indent_str + f"{json.dumps(k)}: {self.encode(v)}" for k, v in o.items()]
				self.indentation_level -= 1
				return "{\n" + ",\n".join(output) + "\n" + self.indent_str + "}"
			else:
				return "{}"
		elif isinstance(o, IdleonModel):
			type_str = f"<{o.__class__.__name__}Model>"
			self.needToImport.add(f"{o.__class__.__name__}Model")
			if o:
				output = [f"{json.dumps(k)}: {self.encode(v)}" for k, v in o]
				if self._put_on_single_line(output):
					return type_str + "{" + ", ".join(output) + "}"
				self.indentation_level += 1
				output = [self.indent_str + f"{json.dumps(k)}: {self.encode(v)}" for k, v in o]
				self.indentation_level -= 1
				return type_str + "{\n" + ",\n".join(output) + "\n" + self.indent_str + "}"
			else:
				return type_str + "{}"
		elif isinstance(o, enum.Enum):
			self.needToImport.add(f"{o.__class__.__name__}")
			return f"{o.__class__.__name__}.{o.name}"
		elif isinstance(o, float):  # Use scientific notation for floats, where appropiate
			return format(o, "g")
		elif isinstance(o, str):  # escape newlines
			o = o.replace("\n", "\\n")
			o = o.replace("\\", "")
			return f'"{o}"'
		else:
			return json.dumps(o)

	def _put_on_single_line(self, o):
		return self._primitives_only(o) and len(o) <= self.MAX_ITEMS and len(str(o)) - 2 <= self.MAX_WIDTH

	def _primitives_only(self, o: Union[list, tuple, dict]):
		if isinstance(o, (list, tuple)):
			return not any(isinstance(el, self.CONTAINER_TYPES) for el in o)
		elif isinstance(o, dict):
			return not any(isinstance(el, self.CONTAINER_TYPES) for el in o.values())

	@property
	def indent_str(self) -> str:
		return self.INDENTATION_CHAR * (self.indentation_level * self.indent + self.base_indent)
