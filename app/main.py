import pkgutil
from fastapi import FastAPI
import app.routes as routes

api = FastAPI(
    title="belingapi",
    description="Api for belinger",
    contact={
        "name": "I.M. Beniamin",
        "email": "beniiorga@gmail.com",
    },

)
for loader, name, is_pkg in pkgutil.walk_packages(routes.__path__):
    if is_pkg:
        continue
    __import__(f"app.routes.{name}")
    api.include_router(getattr(getattr(routes, name), "router"), prefix=f"/api/v1")
    print(f"{name} included")
