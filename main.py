from fastapi import FastAPI, Depends
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session
app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "Welcome to Storage Trac"

products=[
    Product(id=1,name="phone",description="budget phone",price=99,quantity=10),
    Product(id=2,name="laptop",description="gaming laptop",price=999,quantity=5),
    Product(id=3,name="headphone",description="for streaming and gammin",price=40,quantity=15),
    Product(id=4,name="smartWatch",description="smart wearables",price=70,quantity=7),
]
def get_db():
    db = session()
    try: 
        yield db
    finally: 
        db.close()
def init_db():
    db = session() 
    count = db.query(database_models.Product).count
    if count ==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()
@app.get("/products")
def get_all_product(db:Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products
@app.get("/product/{id}")
def get_product_by_id(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product  
    return "product not found"

@app.post("/product")
def add_product(product: Product,db:Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product 
@app.put("/product")
def update_product(id: int,product: Product,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name = product.name 
        db_product.description = product.description 
        db_product.price = product.price 
        db_product.quantity = product.quantity 
        db.commit()
        return "product added successfully"
        
    else:
        return "no product found"

@app.delete("/product")
def delete_product_by_id(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            return "deleted successfully"
    return "no product found"