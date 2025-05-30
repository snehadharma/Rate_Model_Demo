from pydantic import BaseModel
from datetime import date
from functools import cache
from pathlib import Path

import pydantic
from fastapi import APIRouter
from fastui import AnyComponent, FastUI
from fastui import components as c
from fastui.components.display import DisplayLookup, DisplayMode
from fastui.events import BackEvent, GoToEvent
from pydantic import BaseModel, Field, TypeAdapter

from header import demo_page

router = APIRouter()


class Route(BaseModel):
    id: int
    name: str
    customer: str
    origin: str
    load_port: str
    discharge_port: str
    redelivery: str

# @cache 
def routes_list() -> list[Route]:
    print("made it to routes list")
    routes_adapter = TypeAdapter(list[Route])
    routes_file = Path(__file__).parent / 'routes.json'
    print(f"Looking for file at: {routes_file}")
    print(f"File exists: {routes_file.exists()}")
    routes = routes_adapter.validate_json(routes_file.read_bytes())
    # routes.sort(key=lambda city: city.population, reverse=True)
    return routes

# TODO add filter functionality with FilterForm

@router.get('/table/routes', response_model=FastUI, response_model_exclude_none=True)
def routes_view(page: int = 1) -> list[AnyComponent]:
    print("looking for routes")
    routes = routes_list()
    page_size = 1
    return demo_page(
        c.Table(
            data=routes[(page - 1) * page_size : page * page_size],
            data_model=Route, 
            columns=[
                DisplayLookup(field='name', table_width_percent=16), 
                DisplayLookup(field='customer', table_width_percent=16),
                DisplayLookup(field='origin', table_width_percent=16), 
                DisplayLookup(field='load_port', table_width_percent=16),
                DisplayLookup(field='discharge_port', table_width_percent=16), 
                DisplayLookup(field='redelivery', table_width_percent=16)
            ]
        ),
        title='Routes'
    )