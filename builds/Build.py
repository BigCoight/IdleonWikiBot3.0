from typing import Dict, List

from definitions.master.IdleonModel import IdleonModel


class Talent(IdleonModel):
	level: int
	note: str


class Tab(IdleonModel):
	name: str
	talents: Dict[str, Talent]
	note: str


class Build(IdleonModel):
	title: str
	notes: str
	version: str
	level: int
	tabs: List[Tab]
	idleonClass: str


