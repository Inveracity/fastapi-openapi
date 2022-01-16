from typing import Dict, List
from pydantic import BaseModel

class ItemResponse(BaseModel):
    item_name: str
