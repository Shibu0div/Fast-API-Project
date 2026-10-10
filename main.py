from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Storage Trac"

products=[
    Product(id=1,name="phone",description="budget phone",price=99,quantity=10),
    Product(id=2,name="laptop",description="gaming laptop",price=999,quantity=5),
    Product(id=3,name="headphone",description="for streaming and gammin",price=40,quantity=15),
    Product(id=4,name="smartWatch",description="smart wearables",price=70,quantity=7),
]

@app.get("/products")
def get_all_product():
    return products
@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if id == product.id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product 
@app.put("/product")
def update_product(id: int,product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
    return "no product found"

@app.delete("/product")
def delete_product_by_id(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            return "deleted successfully"
    return "no product found"