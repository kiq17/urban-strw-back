from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey, Float
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    update_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    a_venda = Column(Boolean, server_default="TRUE")
    coverImg = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    visitas = Column(Integer, server_default="0")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    update_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    user = relationship("User")

class ProductsImages(Base):
    __tablename__ = "products_images"
    
    id = Column(Integer, primary_key=True, nullable=False)
    image_url = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))


class FavoriteProducts(Base):
    __tablename__ = "favorite_products"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    product = relationship("Product")

class ProductDetails(Base):
    __tablename__ = "products_details"

    id = Column(Integer, primary_key=True, nullable=False)
    modelo = Column(String, nullable=False)
    composicao = Column(String, nullable=False)
    info = Column(String, nullable=False)
    fabricacao = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))


class Preferences(Base):
    __tablename__ = "peferences"

    id = Column( Integer, primary_key=True, nullable=False)
    choice = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

class Otps(Base):
    __tablename__ = "otps"

    id = Column( Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    temp_link = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    product = relationship("Product")