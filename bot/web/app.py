from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from bot.services.event_service import list_events

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(
    title="ATLAS Dashboard",
    version="0.1.0",
)

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/eventos")
async def eventos() -> list[dict]:
    return list_events()