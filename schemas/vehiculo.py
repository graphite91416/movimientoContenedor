from pydantic import BaseModel, Field
from typing import Optional

class Vehiculo(BaseModel):
    id: Optional[int] = None
    placa: str = Field(min_length=6, max_length=10)