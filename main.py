from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "hello"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"user {user_id}"
    }

@app.get("/products/search")
def search_products(keyword: str | None = None, limit: int = 10):
    return{
        "keyword" : keyword,
        "limit" : limit
    }


@app.get("/products/{product_id}")
def get_product(product_id : int):
    return { 
        "product_id" : product_id,
        "name" : f"product-{product_id}"
    }

