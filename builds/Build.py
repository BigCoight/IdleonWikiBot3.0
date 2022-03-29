from typing import Dict, List

from definitions.master.IdleonModel import IdleonModel


class BuildTalent(IdleonModel):
	name: str
	skillIndex: int
	level: int
	note: str


class BuildTab(IdleonModel):
	name: str
	talents: List[BuildTalent]
	note: str


class Build(IdleonModel):
	title: str
	notes: str
	version: str
	level: int
	tabs: List[BuildTab]
	idleonClass: str


