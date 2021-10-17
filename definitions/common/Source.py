from pydantic import BaseModel


class Source(BaseModel):
    wikiName: str
    txtName: str
