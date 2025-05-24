from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .. import auth, models
from ..database import get_db
from ..schemas.favoriteSchema import CartRes, FavoriteRes
from typing import List

router = APIRouter(prefix="/cart", tags=["cart"])

@router.get("/", response_model=List[CartRes])
def find_cart(user: int = Depends(auth.getCurrentUser), db: Session= Depends(get_db)):
    find_product_in_cart = db.query(models.Cart).filter(models.Cart.user_id == user.id).all()
    
    sum_price = sum(item.product.__dict__["preco"] for item in find_product_in_cart)

    for item in find_product_in_cart:
        item.__dict__.update({"qtd": len(find_product_in_cart), "total": sum_price})


    return find_product_in_cart
    
@router.post("/toggle/{product_id}", response_model=List[FavoriteRes])
def toggle_cart(product_id: int,user: int = Depends(auth.getCurrentUser), db: Session= Depends(get_db)):
    find_product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if find_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    checkAction = db.query(models.Cart).filter(models.Cart.product_id == product_id, models.Cart.user_id == user.id)

    itemFavorite = checkAction.first()
    
    if itemFavorite is None:
        f = models.Cart(product_id=product_id, user_id=user.id)
        db.add(f)
        db.commit()
        return JSONResponse(status_code=201, content={"message": "adicionado ao carrinho"})
    else:
        checkAction.delete(synchronize_session=False)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "removido do carrinho"})
   
