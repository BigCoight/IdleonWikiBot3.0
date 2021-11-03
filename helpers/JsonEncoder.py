import json
from enum import Enum
from typing import Union

from pydantic import BaseModel


class CompactJSONEncoder(json.JSONEncoder):
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
		self.indentation_level = 0

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
		elif isinstance(o, BaseModel):
			return self.encode(o.dict())
		elif isinstance(o, Enum):
			return f'"{o.name}"'
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
		return self.INDENTATION_CHAR * (self.indentation_level * self.indent)
