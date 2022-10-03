from fastapi import APIRouter, Request
# from db_handler import Database
from fastapi.responses import JSONResponse
from rich.console import Console

# --- Constants --- #

app = APIRouter(tags=["XXX"])
console = Console()

# --- Routes --- #

@app.get("/ping")
async def ping() -> dict:
    return {"status": True}

# -------------- #