import os

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pygeoapi.util import yaml_load

if "PYGEOAPI_CONFIG" not in os.environ:
    raise RuntimeError("PYGEOAPI_CONFIG environment variable not set")

with open(os.environ.get("PYGEOAPI_CONFIG"), encoding="utf-8") as f:
    CONFIG = yaml_load(f)

with open(os.environ.get("PYGEOAPI_OPENAPI"), encoding='utf8') as ff:
    if os.environ.get("PYGEOAPI_OPENAPI").endswith(('.yaml', '.yml')):
        openapi_ = yaml_load(ff)
    else:  # JSON file, do not transform
        openapi_ = ff


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="pygeoapi demo",
        version="0.1.0",
        routes=app.routes
    )
    app.openapi_schema = {**openapi_schema, **openapi_}
    return app.openapi_schema
