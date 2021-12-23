from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel


class Source(IdleonModel):
    wikiName: str
    txtName: str
