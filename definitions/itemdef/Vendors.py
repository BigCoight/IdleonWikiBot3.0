from typing import List
from pydantic import BaseModel


class Vendor(BaseModel):
    vendor: str
    quantity: int
    no: int


class Vendors(BaseModel):
    vendors: List[Vendor]
