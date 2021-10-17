from typing import Union

import numpy as np
from pydantic import BaseModel

from definitions.Validators import validateInteger


class Integer(int):
	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if isinstance(v, int):
			return v
		return validateInteger(v)

Numeric = Union[Integer, float]

