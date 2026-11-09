from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


input_data = {"id": 101, "name": "Laptop", "price": 999.99, "in_stock": True}
product = Product(**input_data)
print(product)
