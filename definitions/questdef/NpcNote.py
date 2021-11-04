from typing import Dict

from definitions.common.Note import Note
from definitions.master.IdleonModel import IdleonModel


class NpcNote(IdleonModel):
	notes: Dict[str, Note]
