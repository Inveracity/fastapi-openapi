from fastapi import FastAPI
from fastapi.routing import APIRoute
from milk.routers import items


app = FastAPI(title="milk", description="Milk API", version="0.0.1")

def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name

app.include_router(items.router)
use_route_names_as_operation_ids(app)
