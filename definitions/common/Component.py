from pydantic import BaseModel


class Component(BaseModel):
    """
    item: str
    quantity: int
    """
    item: str
    quantity: int

