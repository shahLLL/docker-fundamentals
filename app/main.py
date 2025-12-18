from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import time

app = FastAPI(title="Dockerized FastAPI")

START_TIME = time.time()
ITEMS = []

class Item(BaseModel):
    name: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[Item])
def list_items():
    return ITEMS

@app.post("/items", response_model=Item, status_code=201)
def add_item(item: Item):
    ITEMS.append(item)
    return item

@app.get("/metrics")
def metrics():
    uptime_seconds = int(time.time() - START_TIME)
    return {
        "uptime_seconds": uptime_seconds,
        "items_count": len(ITEMS),
    }
