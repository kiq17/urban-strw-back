from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from wonderwords import RandomWord

from .. import models
from ..database import get_db
from ..schemas.productSchema import (Product, ProductDetails, ProductImage,
                                     ProductRes)

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/list/")
def get_products(page: int, per_page: int, db: Session = Depends(get_db)):

    oset = 0
    if page == 1:
        page = 0

    if page > 1:
        oset = page - 1

    produtcs = db.query(models.Product).order_by(
        models.Product.visitas.desc()).offset(oset * per_page).limit(per_page).all()

    count = db.query(models.Product).count()

    return {"products": produtcs, "count": count}


@router.get("/")
def search_product(category: Optional[str] = None, name: Optional[str] = None, price: Optional[str] = None, order: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, db: Session = Depends(get_db)):
    to_arr = []
    filter_product = []
    count = db.query(models.Product).count()
    
    finded = 0

    if (category):
        to_arr = category.split(",")

    if (len(to_arr) == 5):
        filter_product = db.query(models.Product).filter((models.Product.categoria.icontains(to_arr[0])) | (
            models.Product.categoria.icontains(to_arr[1])) | (models.Product.categoria.icontains(to_arr[2])) | (models.Product.categoria.icontains(to_arr[3])) | (models.Product.categoria.icontains(to_arr[4]))).all()
    elif (len(to_arr) == 4):
        filter_product = db.query(models.Product).filter((models.Product.categoria.icontains(to_arr[0])) | (
            models.Product.categoria.icontains(to_arr[1])) | (models.Product.categoria.icontains(to_arr[2])) | (models.Product.categoria.icontains(to_arr[3]))).all()
    elif (len(to_arr) == 3):
        filter_product = db.query(models.Product).filter((models.Product.categoria.icontains(to_arr[0])) | (
            models.Product.categoria.icontains(to_arr[1])) | (models.Product.categoria.icontains(to_arr[2]))).all()
    elif (len(to_arr) == 2):
        filter_product = db.query(models.Product).filter((models.Product.categoria.icontains(to_arr[0])) | (
            models.Product.categoria.icontains(to_arr[1]))).all()
    elif (len(to_arr) == 1):
        filter_product = db.query(models.Product).filter(
            (models.Product.categoria.icontains(to_arr[0]))).all()

    if (name):
        #significa que já existe um array com dados
        if (len(to_arr) > 0):
            filter_product = list(
                filter(lambda item:  name in item.nome.lower(), filter_product))
        else:
            filter_product = db.query(models.Product).filter(
                models.Product.nome.icontains(f"{name}")).all()
            
        count = len(filter_product)
    

    if (price):
        split = price.split(",")

        if (len(filter_product) > 0):
            if (len(split) < 1):
                bigger = float(split[0])
                filter_product = list(
                    filter(lambda item:  bigger <= item.preco <= 0, filter_product))
            else:
                lower = float(split[1])
                filter_product = list(
                    filter(lambda item:  float(split[0]) <= item.preco <= float(split[1]), filter_product))


        #verificando se só tem filtro de price
        if (len(split) <= 1):
            filter_product = db.query(models.Product).filter(
            models.Product.preco.between(0, float(split[0]))).order_by(models.Product.preco).all()
            finded = len(filter_product)
        else:
            bigger = float(split[0])
            lower = float(split[1])
            filter_product = db.query(models.Product).filter(
            models.Product.preco.between(bigger, lower)).order_by(models.Product.preco).all()
            # filter_product = list(
            #     filter(lambda item:  bigger <= item.preco <= lower, filter_product))
        
        #condições caso o filtro de price esteja adicionado a outros filtros
         

    if (order):
        if ((len(to_arr) > 0 or name or price) and order == "recente"):
            filter_product.sort(reverse=True, key=lambda item: item.created_at)
        elif ((len(to_arr) > 0 or name or price) and order == "relevante"):
            filter_product.sort(reverse=True, key=lambda item: item.visitas)
        elif (order == "recente"):
            filter_product = db.query(models.Product).order_by(
                models.Product.created_at.desc()).all()
        elif (order == "relevante"):
            filter_product = db.query(models.Product).order_by(
                models.Product.visitas.desc()).all()
        elif (order == "maior"):
            filter_product = db.query(models.Product).order_by(
                models.Product.preco.desc()).all()
        elif (order == "menor"):
            filter_product = db.query(models.Product).order_by(
                models.Product.preco.asc()).all()
            
        count = len(filter_product)

    if (page and per_page):
        filter_product = filter_product[(page-1) * per_page:page*per_page]

    # if(not category and not name and not price and not order):
    #     oset = 0

    #     if page == 1:
    #         page = 0

    #     if page > 1:
    #         oset = page - 1

    #     produtcs = db.query(models.Product).order_by(models.Product.visitas.desc()).offset(oset * per_page).limit(per_page).all()

    #     return {"products": produtcs, "finded": 6, "count": count}

    # filter with category and order not working
    if (category and order):
        # lambda function to filter array of products
        # added just the first category, had to add the others
        # probably using a for loop
        result = []
        for c in to_arr:
            for p in filter_product:
                if c.capitalize() == p.categoria:
                    result.append(p)
        filter_product = result

    if (len(filter_product) < count and len(to_arr) > 0):
        print("nem", count)
        return {"products": filter_product, "finded": len(filter_product), "count": len(filter_product)}

    print("fin", count, len(filter_product))
    return {"products": filter_product, "finded": len(filter_product), "count": count}


@router.get("/details/{id}")
def get_details_products(id: int, db: Session = Depends(get_db)):
    find_product = db.query(models.ProductDetails).filter(
        models.ProductDetails.product_id == id).first()

    if find_product is None:
        raise HTTPException(400, "Produto não encontrado")

    return find_product
    # retornar detalhas de fabricação e quantos vezes o produto foi favoritado


@router.get("/{slug}")
def get_product(slug: str, db: Session = Depends(get_db)):
    find_product = db.query(models.Product).filter(
        models.Product.slug == slug)

    product = find_product.first()

    if product is None:
        raise HTTPException(400, "Produto não encontrado")

    favorites = db.query(func.count(models.FavoriteProducts.product_id)).filter(
        models.FavoriteProducts.product_id == product.id).all()

    find_product.update({"visitas": product.visitas + 1},
                        synchronize_session=False)

    db.commit()
    db.refresh(product)

    f = favorites[0]
    copy_product = product.__dict__
    copy_product["favorites"] = f[0]

    return copy_product


@router.delete("/{product_id}", status_code=204)
def del_product(product_id: int, db: Session = Depends(get_db)):
    find_product = db.query(models.Product).filter(
        models.Product.id == product_id)

    product = find_product.first()

    if product is None:
        raise HTTPException(400, "Produto não encontrado")

    find_product.delete(synchronize_session=False)
    db.commit()

    return


@router.post("/", status_code=201, response_model=ProductRes)
def new_product(product: Product, db: Session = Depends(get_db)):
    w = RandomWord()
    copy_product = product.dict()
    words = w.random_words(4, word_min_length=5)

    copy_product["slug"] = "-".join(words)

    p = models.Product(**copy_product)
    db.add(p)
    db.commit()
    db.refresh(p)

    return p


@router.post("/image/{product_id}", status_code=201)
def add_image_to_product(product_id: int, product_img: ProductImage, db: Session = Depends(get_db)):
    find_producut = db.query(models.Product).filter(
        models.Product.id == product_id)

    if find_producut is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")

    p = models.ProductsImages(
        image_url=product_img.image_url, product_id=product_id)
    db.add(p)
    db.commit()

    return {"message": "imagem adiciona ao produto"}


@router.get("/images/{slug}", response_model=List[ProductImage])
def images(slug: str, db: Session = Depends(get_db)):
    find_producut = db.query(models.Product).filter(
        models.Product.slug == slug).first()

    product_imgs = db.query(models.ProductsImages).filter(
        models.ProductsImages.product_id == find_producut.id).all()

    if product_imgs is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")

    product_imgs.insert(0, {"image_url": find_producut.coverImg})

    return product_imgs


@router.post("/details/{product_id}")
def product_details(product: ProductDetails, product_id: int, db: Session = Depends(get_db)):
    find_producut = db.query(models.Product).filter(
        models.Product.id == product_id)

    if find_producut is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")

    p = models.ProductDetails(**product.dict(), product_id=product_id)
    db.add(p)
    db.commit()
    db.refresh(p)

    return p


@router.put("/edit/{product_id}", response_model=ProductRes)
def edit_product(product_id: int, product: dict = Body(...), db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(
        models.Product.id == product_id)

    find_product = product_query.first()

    if find_product is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")

    dict_product = find_product.__dict__
    # checando se valores existem
    for key_p in product:
        if dict_product.get(key_p) is None:
            raise HTTPException(
                status_code=400, detail="Elemento enviado é inválido")

    # transferindo valores
    for key in dict_product:
        for key_b in product:
            if key_b == key:
                dict_product[key_b] = product[key]

    dict_product.pop("_sa_instance_state")
    dict_product["update_at"] = datetime.now()
    dp = models.Product(**dict_product)

    product_query.update(dict_product, synchronize_session=False)

    db.commit()

    return dp
