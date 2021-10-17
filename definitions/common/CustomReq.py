from pydantic import BaseModel

from helpers.CustomTypes import Integer


class CustomReq(BaseModel):
	desc: str
	finalV: Integer
	type: str
	startV: Integer