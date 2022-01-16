from fastapi import APIRouter, Response
from typing import List, Dict
from milk.models.items import ItemResponse
from milk.db import fake_items_db


router = APIRouter()


@router.get("/items/", response_model=List[ItemResponse])
async def read_item(skip: int = 0, limit: int = 10):
    """
    - **skip**: how many items to skip
    - **limit**: how many items to show
    """
    return fake_items_db[skip : skip + limit]
