from typing import Union

from definitions.Validators import validateInteger


class Integer(int):
	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if isinstance(v, int):
			return v
		if isinstance(v, float) and v.is_integer():
			return int(v)
		try:
			return validateInteger(v)
		except ValueError:
			try:
				return float(v)
			except ValueError:
				return -1


Numeric = Union[Integer, float]
