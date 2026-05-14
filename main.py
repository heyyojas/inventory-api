from fastapi import FastAPI
from models import Products
from database import session, engine
import database_models


app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Products(id = 1, name = "Phone", description =  "budget Phone", price = 99, quantity =  5),
    Products(id = 2, name = "Laptop", description =  "budget Laptop", price = 199, quantity =  2),
    Products(id = 3, name = "Pen", description =  "Blue ink Pen", price = 1, quantity =  100),
    Products(id = 4, name = "Table", description =  "wooden table ", price = 29, quantity =  9),
]

def init_db():
    db = session()

    count = db.query(database_models.Products).count


    if count == 0: 
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
               
        
    db.commit()
               

init_db()

@app.get("/products")
def get_all_products(): 
    # db connection
    db = session()
    # query
    db.query()
    return products

@app.get("/product/{id}")
def get_product_by_id(id : int):
    for product in products: 
        if product.id == id:
            return product
        
    return "product not found"


@app.post("/product")
def add_product(product: Products):
    products.append(product)
    return product

@app.put("/product")
def update_product(id : int, product: Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"
        
        return "Product Not Found"
    
@app.delete("/product")
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Successfully Deleted"
        
        return "Product Not Found, Not Deleted"