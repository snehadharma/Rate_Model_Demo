from __future__ import annotations as _annotations

import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.auth import fastapi_auth_exception_handling
from fastui.components.display import DisplayLookup, DisplayMode
from fastui.dev import dev_fastapi_app
from httpx import AsyncClient
from pydantic import BaseModel, TypeAdapter

from index import router as index_router
from table import router as table_router 
from addroute import router as add_router 
from fastapi.middleware.cors import CORSMiddleware

from header import demo_page

version = "v1"
# app = FastAPI(
#     version=version
# )

# app = FastAPI()

@asynccontextmanager
async def lifespan(app_: FastAPI):
    async with AsyncClient() as client:
        app_.state.httpx_client = client
        yield


frontend_reload = '--reload' in sys.argv
if frontend_reload:
    # dev_fastapi_app reloads in the browser when the Python source changes
    app = dev_fastapi_app(lifespan=lifespan)
else:
    app = FastAPI(lifespan=lifespan)

    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(index_router, prefix="/api")
app.include_router(table_router, prefix='/api/table/routes')
app.include_router(add_router, prefix='/api/addroute')



@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Rate Model Demo'))