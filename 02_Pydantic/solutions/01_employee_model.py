from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)


emp = Employee(id=1, name="Khizer", department="HR", salary=12000)
print(emp)
