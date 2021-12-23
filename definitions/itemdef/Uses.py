from typing import List, Union

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel


class _Use(IdleonModel):
    name: str
    amount: Union[int, str]
    type: str


class Uses(IdleonModel):
    uses: List[_Use]
