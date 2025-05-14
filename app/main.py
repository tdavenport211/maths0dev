# main.py
# https://fastapi.tiangolo.com/tutorial/bigger-applications/
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import textbook, items, users

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(textbook.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
#configure_staticfiles(app)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

