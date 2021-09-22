from pydantic import BaseModel


class AnvilProduce(BaseModel):
    no: int
    time: int
    levelReq: int
    exp: int
