import pkgutil
from fastapi import FastAPI
import routes
app = FastAPI(
    title="belingapi",
    description="Api for belinger",
    contact={
        "name": "I.M. Beniamin",
        "url": "https://www.derpi.it/#contact",
        "email": "beniiorga@gmail.com",
    },

)
for loader, name, is_pkg in pkgutil.walk_packages(routes.__path__):
    if is_pkg:
        continue
    __import__(f"routes.{name}")
    app.include_router(getattr(getattr(routes, name), "router"), prefix=f"/api/v1")
    print(f"{name} included")
