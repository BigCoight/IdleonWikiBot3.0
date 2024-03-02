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
				return Integer(float(v))
			except ValueError:
				return -1

	def __repr__(self):
		res = np.format_float_positional(float(self))
		if res[-1] == ".":
			return res[:-1]
		return res

	def __str__(self):
		return self.__repr__()


Numeric = Union[Integer, float]
