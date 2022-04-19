from functools import partial

from fastapi import FastAPI
from fastapi_opa import OPAMiddleware
from pygeoapi.starlette_app import app as pygeoapi
from starlette.middleware.cors import CORSMiddleware

# import authenticate
from utils import custom_openapi
import test
app = FastAPI()

# app.include_router(authenticate.router)
app.openapi = partial(custom_openapi, app)


origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(path="/v1", app=pygeoapi)
# app.add_middleware(OPAMiddleware, config=authenticate.opa_config,
#                    skip_endpoints=authenticate.skip_endpoints)



