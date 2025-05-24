from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade: int
    coverImg: str
    categoria: str

class ProductRes(Product):
    id: int
    a_venda: bool
    created_at: datetime
    update_at: datetime
    slug: Optional[str]

    class Config:
        orm_mode = True

class ProductImage(BaseModel):
    image_url: str

    class Config:
        orm_mode = True

class ProductDetails(BaseModel):
    modelo: str
    composicao: str
    info: str
    fabricacao: str

    class Config:
        orm_mode = True