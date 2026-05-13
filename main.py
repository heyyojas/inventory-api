from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Products(id = 1, name = "Phone", description =  "budget Phone", price = 99, quantity =  5),
    Products(id = 2, name = "Laptop", description =  "budget Laptop", price = 199, quantity =  2),
    Products(id = 3, name = "Pen", description =  "Blue ink Pen", price = 1, quantity =  100),
    Products(id = 4, name = "Table", description =  "wooden table ", price = 29, quantity =  9),
]

@app.get("/products")
def get_all_products(): 
    return products