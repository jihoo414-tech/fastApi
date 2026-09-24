from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ProductCreateRequest(BaseModel):
    name : str
    price : int

@app.post("/products")
def create_product(request: ProductCreateRequest):
    return{
        "name": request.name,
        "price": request.price
    }