from typing import List

from pydantic import BaseModel

from definitions.common.Drop import Drop


class DropTable(BaseModel):
	drops: List[Drop]
