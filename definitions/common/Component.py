from pydantic import BaseModel
from helpers.CustomTypes import Integer


class Component(BaseModel):
    """
    item: str
    quantity: int
    """
    item: str
    quantity: Integer

