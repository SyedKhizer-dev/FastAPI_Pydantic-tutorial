from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    id: int
    name: str
    location: str


data: list[Data] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Data API!"}


@app.get("/data")
def get_data():
    return data


@app.post("/data")
def add_data(item: Data):
    data.append(item)
    return item


@app.put("/data/{data_id}")
def update_data(data_id: int, updated_data: Data):
    for index, data_item in enumerate(data):
        if data_item.id == data_id:
            data[index] = updated_data
            return updated_data
    return {"error": "Data not found"}


@app.delete("/data/{data_id}")
def delete_data(data_id: int):
    for index, data_item in enumerate(data):
        if data_item.id == data_id:
            deleted_item = data.pop(index)
            return deleted_item
    return {"error": "Data not found"}
