from __future__ import annotations as _annotations

from fastapi import APIRouter
from fastui import AnyComponent, FastUI
from fastui import components as c

from header import demo_page

router = APIRouter()

@router.get('/', response_model=FastUI, response_model_exclude_none=True)
def api_index() -> list[AnyComponent]:
    markdown = """\ Welcome to the Rate Model Demo! """
    return demo_page(c.Markdown(text=markdown))

@router.get('/{path:path}', status_code=404)
async def api_404():
    # so we don't fall through to the index page
    return {'message': 'Not Found'}