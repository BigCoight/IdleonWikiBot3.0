from typing import List, Union

from pydantic import BaseModel


class _Use(BaseModel):
    name: str
    amount: Union[int, str]
    type: str


class Uses(BaseModel):
    uses: List[_Use]
