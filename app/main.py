import pkgutil
from fastapi import FastAPI
import app.routes as routes
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(
    title="belingapi",
    description="Api for belinger",
    contact={
        "name": "I.M. Beniamin",
        "email": "beniiorga@gmail.com",
    })

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for loader, name, is_pkg in pkgutil.walk_packages(routes.__path__):
    if is_pkg:
        continue
    __import__(f"app.routes.{name}")
    api.include_router(getattr(getattr(routes, name), "router"), prefix=f"/api/v1")
    print(f"{name} included")
