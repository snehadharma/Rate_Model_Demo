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


router.get("/", response_class=FastUI, response_model_exclude_none=True)
def add_router() -> list[AnyComponent]:
    markdown = """Insert add route fuctionality here."""
    return demo_page(c.Markdown(text=markdown))