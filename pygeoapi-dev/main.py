
from fastapi import FastAPI
from pygeoapi.starlette_app import app as pygeoapi
import authenticate
app = FastAPI(
    title="AuthX",
    description="AuthX is a simple authentication system for fastapi.",
    version="0.1.0",
)


app.include_router(authenticate.router)
app.mount(path="/v1", app=pygeoapi)