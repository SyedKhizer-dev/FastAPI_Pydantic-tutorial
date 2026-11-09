from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    addresses: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime(
                "%d-%m-%Y %H:%M:%S"
            )  # Custom encoder for datetime
        }
    )


user = User(
    id=1,
    name="Khizer",
    email="khizer@gmail.com",
    is_active=True,
    createdAt=datetime.now(),
    addresses=Address(street="123 Main St", city="New York", zip_code="10001"),
    tags=["premium", "subscriber"],
)


# print("User:", user)
print(type(user))

# Using model_dump to serialize the user object to a dictionary
python_dict = user.model_dump()
# print("Serialized to Python dict:", python_dict)
print(type(python_dict))

# Using model_dump_json to serialize the user object to a JSON string
json_string = user.model_dump_json()
print("Serialized to JSON string:", json_string)
print(type(json_string))
