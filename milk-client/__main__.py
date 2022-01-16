from milk_client import Client
from milk_client.api.default import read_item
from milk_client.models import ItemResponse
from milk_client.types import Response

c = Client("http://127.0.0.1:8000", timeout=120.0, verify_ssl=False)


def process_items():
    res = read_item.sync(client=c, skip=0, limit=1)

    if res is None:
        return

    for r in res:
        if isinstance(r, ItemResponse):
            print(f"heck yeah {r.item_name}")

if __name__ == "__main__":
    process_items()
