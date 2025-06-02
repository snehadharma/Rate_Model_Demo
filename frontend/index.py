from __future__ import annotations as _annotations

from pathlib import Path
from fastapi import APIRouter
from fastui import AnyComponent, FastUI
from fastui import components as c
from pydantic import BaseModel, TypeAdapter
from fastui.components.display import DisplayLookup, DisplayMode
from functools import cache

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

@cache 
def routes_list() -> list[Route]:
    routes_adapter = TypeAdapter(list[Route])
    routes_file = Path(__file__).parent / 'routes.json'
    routes = routes_adapter.validate_json(routes_file.read_bytes())
    # routes.sort(key=lambda city: city.population, reverse=True)
    return routes

# TODO add filter functionality with FilterForm


@router.get('/', response_model=FastUI, response_model_exclude_none=True)
def api_index() -> list[AnyComponent]:
    routes = routes_list()
    page_size = 1
    return demo_page(
        c.Table(
            data=routes,
            data_model=Route, 
            columns=[
                DisplayLookup(field='name', table_width_percent=17), 
                DisplayLookup(field='customer', table_width_percent=16),
                DisplayLookup(field='origin', table_width_percent=16), 
                DisplayLookup(field='load_port', table_width_percent=16),
                DisplayLookup(field='discharge_port', table_width_percent=16), 
                DisplayLookup(field='redelivery', table_width_percent=16)
            ]
        ),
        title='Routes'
    )
    # markdown = """Welcome to the Rate Model Demo!"""
    # return demo_page(c.Markdown(text=markdown))

@router.get('/{path:path}', status_code=404)
async def api_404():
    # so we don't fall through to the index page
    return {'message': 'Not Found'}