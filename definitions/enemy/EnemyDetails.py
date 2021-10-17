from typing import Tuple, Union, Dict, Callable

from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class EnemyDetails(IdleonModel):
	Name: str
	AFKtype: str
	MonsterFace: Integer
	MonsterOffsetX: Integer
	MonsterOffsetY: Integer
	HeightOfMonster: Integer
	MonsterMoving: Integer
	MovingFrame: Integer
	RespawnTime: Integer
	DeathFrame: Integer
	MonsterHPTotal: Integer
	Type: str
	SpecialType: str
	ExpGiven: Integer
	ExpType: Integer
	Defence: Integer
	MoveSPEED: Integer
	Damages: Tuple[Integer, Integer]
	DefFor0: Integer = 0

	@validator("DefFor0", always = True, )
	def defFor0(cls, _, values):
		y = int(values["Damages"][0])

		def f1(x):
			return x ** 2.5 + 500 * y * x ** 0.8 - 200 * y ** 2 + 100 * y

		def f2(x):
			return 2.5 * x ** 1.5 + 400 * y * x ** -0.2

		z = 1
		eps = 1e-1
		while abs(f1(z) / f2(z)) > eps:
			z = z - f1(z) / f2(z)
		return round(z, 2)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"image": self.getImage,
			"attack": self.getAttack,
			"health": "MonsterHPTotal",
			"defence": "Defence",
			"speed": "MoveSPEED",
			"exp": "ExpGiven",
			"respawn": "RespawnTime",
			"defence0": "DefFor0",
		}

	def getImage(self) -> str:
		return f"{self.Name} Walking.gif"

	def getAttack(self) -> str:
		return f"{self.Damages[0]}"
