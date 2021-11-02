from typing import List

from definitions.common.Note import Note
from definitions.master.IdleonModel import IdleonModel


class NpcNote(IdleonModel):
	notes: List[Note]
