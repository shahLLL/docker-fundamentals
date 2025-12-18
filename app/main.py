from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List
import os
import time

APP_NAME = "Dockerized FastAPI"
API_VERSION = os.getenv("API_VERSION", "1.0.0")   # semantic version
API_PREFIX = os.getenv("API_PREFIX", "/v1")       # route versioning

app = FastAPI(
    title=APP_NAME,
    version=API_VERSION,
)

router = APIRouter(prefix=API_PREFIX)

START_TIME = time.time()
ITEMS = []

class Item(BaseModel):
    name: str


class HealthResponse(BaseModel):
    status: str
    api_version: str
    api_prefix: str


class MetricsResponse(BaseModel):
    uptime_seconds: int
    items_count: int

@router.get("/health", response_model=HealthResponse)
def health():
    return {
        "status": "ok",
        "api_version": API_VERSION,
        "api_prefix": API_PREFIX,
        }

@router.get("/items", response_model=List[Item])
def list_items():
    return ITEMS

@router.post("/items", response_model=Item, status_code=201)
def add_item(item: Item):
    ITEMS.append(item)
    return item

@router.get("/metrics", response_model=MetricsResponse)
def metrics():
    uptime_seconds = int(time.time() - START_TIME)
    return {
        "uptime_seconds": uptime_seconds,
        "items_count": len(ITEMS),
    }

app.include_router(router)