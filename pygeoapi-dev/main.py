from functools import partial

from fastapi import FastAPI
from pygeoapi.starlette_app import app as pygeoapi
from utils import custom_openapi

app = FastAPI()
app.openapi = partial(custom_openapi, app)

# app.include_router(utils.router)


# app.include_router(auth.auth_router, prefix="/api/auth", tags=["auth"])
# app.include_router(auth.password_router, prefix="/api/password", tags=["password"])
# app.include_router(auth.admin_router, prefix="/api/admin", tags=["admin"])
# app.include_router(auth.search_router, prefix="/api/search", tags=["search"])

app.mount(path="/v1", app=pygeoapi)
