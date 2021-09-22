from typing import List
from pydantic import BaseModel


class _Vendor(BaseModel):
    vendor: str
    quantity: int
    no: int


class Vendors(BaseModel):
    Vendors: List[_Vendor]
