from fastapi import Depends, FastAPI
from models import Products
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database_models.Base.metadata.create_all(bind = engine)

from fastapi.responses import RedirectResponse

@app.get("/")
def greet():
    return RedirectResponse(url="/app")

products = [
    Products(id = 1, name = "Phone", description =  "budget Phone", price = 99, quantity =  5),
    Products(id = 2, name = "Laptop", description =  "budget Laptop", price = 199, quantity =  2),
    Products(id = 3, name = "Pen", description =  "Blue ink Pen", price = 1, quantity =  100),
    Products(id = 4, name = "Table", description =  "wooden table ", price = 29, quantity =  9),
]

def get_db():
    db = session()
    try: 
        yield db
    finally: 
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Products).count


    if count == 0: 
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
               
        
    db.commit()
               

init_db()

@app.get("/products")
def get_all_products(db: Session  = Depends(get_db)): 
    
    db_products = db.query(database_models.Products).all()

    return db_products

@app.get("/product/{id}")
def get_product_by_id(id : int, db: Session  = Depends(get_db)):
        db_product = db.query(database_models.Products).filter(database_models.Products.id == id).first()
        if db_product:
            return db_product
        return "product not found"


@app.post("/product")
def add_product(product: Products, db: Session  = Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id : int, product: Products, db: Session  = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_product: 
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    else: 
        return "Product Not Found"
    
@app.delete("/product")
def delete_product(id : int, db: Session  = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_product:
            db.delete(db_product)
            db.commit()
            return "Product Successfully Deleted"
    else: 
        return "Product Not Found, Not Deleted"
    
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")