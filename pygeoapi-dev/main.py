
from functools import partial

from fastapi import FastAPI
from pygeoapi.starlette_app import app as pygeoapi
from utils import custom_openapi

app = FastAPI()

# app.include_router(utils.router)


app.openapi = partial(custom_openapi, app)

# app.include_router(auth.auth_router, prefix="/api/users")
# app.include_router(auth.social_router, prefix="/auth")
# app.include_router(auth.password_router, prefix="/api/users")
# app.include_router(auth.admin_router, prefix="/api/users")
# app.include_router(auth.search_router, prefix="/api/users")
#
# app.include_router(authenticate.router)
app.mount(path="/v1", app=pygeoapi)
