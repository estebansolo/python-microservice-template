from pydantic import BaseModel


class Fake(BaseModel):
    id: int
    name: str
