from typing import List

from pydantic import BaseModel


class Sources(BaseModel):
    sources: List[str]
