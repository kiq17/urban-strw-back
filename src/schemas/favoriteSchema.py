from pydantic import BaseModel
from datetime import datetime
from .productSchema import ProductRes

class FavoriteRes(BaseModel):
    product: ProductRes
    created_at: datetime

    class Config:
        orm_mode = True


    

class CartRes(BaseModel):
    product: ProductRes
    created_at: datetime
    total: int
    qtd: int

    class Config:
        orm_mode = True