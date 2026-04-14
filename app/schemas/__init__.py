from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    is_available: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
