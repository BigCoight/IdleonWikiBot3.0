from typing import Union

import numpy as np

from definitions.Validators import validateInteger


class Integer(int):
	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if isinstance(v, int):
			return Integer(v)
		if isinstance(v, float) and v.is_integer():
			return Integer(v)
		try:
			return Integer(validateInteger(v))
		except ValueError:
			try:
				return float(v)
			except ValueError:
				return -1

	def __repr__(self):
		res = np.format_float_positional(float(self))
		if res[-1] == ".":
			return res[:-1]
		return res

	def __str__(self):
		return self.__repr__()


class Boolean:
	def __init__(self, v: bool):
		self.v = v

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if isinstance(v, bool):
			return Boolean(v)
		if v == "1":
			return Boolean(True)
		return Boolean(False)

	def __str__(self):
		return str(self.v)

	@classmethod
	def __modify_schema__(cls, field_schema):
		field_schema.update(type = "boolean", example = "true")


Numeric = Union[Integer, float]
