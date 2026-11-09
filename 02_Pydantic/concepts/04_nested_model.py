from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    addresses: Address


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None  # Recursive relationship


Comment.model_rebuild()

address = Address(street="123 Main St", city="New York", state="NY", zip_code="10001")
user = User(id=1, name="Khizer", addresses=address)
comment1 = Comment(id=1, content="This is a comment.")
comment2 = Comment(id=2, content="This is a reply.", replies=[comment1])

print(f"Address: {address}")
print(f"User: {user}")
print(f"Comment 1: {comment1}")
print(f"Comment 2: {comment2}")
