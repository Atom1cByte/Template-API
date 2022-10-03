import os, uvicorn
from routes import apps
from fastapi import FastAPI
from rich.console import Console

# --- Constants --- #

app = FastAPI()
console = Console()

# --- Import API Routes --- #

for route in apps:
    app.include_router(route)
    console.log("[API] Loaded router: {}".format(route))

# --- Events --- #


@app.on_event("startup")
async def startup():
    console.log("[API] Starting...")


@app.on_event("shutdown")
async def shutdown():
    console.log("[API] Shutting down...")


# --- Home --- #

@app.get("/")
async def home():
    return 200

# --- Running --- #

if __name__ == "__main__":
    uvicorn.run(f"{os.path.basename(__file__).replace('.py', '')}:app", host="0.0.0.0", port=80, reload=True)

