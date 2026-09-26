from pydantic import BaseModel

class ProductCreateRequest(BaseModel):
  name : str
  price : int