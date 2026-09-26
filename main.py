from fastapi import FastAPI

from schemas.user import UserCreateRequest
from schemas.product import ProductCreateRequest
from services.user_service import create_user_service
from services.product_service import create_product_service

app = FastAPI()


@app.post("/users")
def create_user(request: UserCreateRequest):
    return create_user_service(request)

@app.post("/products")
def create_product(request: ProductCreateRequest):
    return create_product_service(request)