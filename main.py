from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))