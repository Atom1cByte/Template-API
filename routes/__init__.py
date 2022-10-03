import os
from rich.console import Console
from fastapi import APIRouter

console = Console()
apps = []

for category in os.listdir("./routes"):
    if category in ["__pycache__", "__init__.py"]:
        continue
    router = APIRouter(prefix="/"+category)
    routes = []
    for route in [file[:-3] for file in os.listdir("./routes/"+category) if file.endswith(".py")]:
        exec(f"from .{category}.{route} import app as route")
        exec("routes.append(route)")
        exec("del route")
    
    for route in routes:
        router.include_router(route)
        console.log(f"[API] Loaded route: {route} into {router}")
    
    apps.append(router)
