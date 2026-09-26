from schemas.product import ProductCreateRequest

def create_product_service(request: ProductCreateRequest):
    return {
        "name": request.name,
        "price": request.price
    }