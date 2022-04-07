import json
import os

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from pygeoapi.util import yaml_load

if "PYGEOAPI_CONFIG" not in os.environ:
    raise RuntimeError("PYGEOAPI_CONFIG environment variable not set")
with open(os.environ.get("PYGEOAPI_CONFIG"), encoding="utf-8") as f:
    CONFIG = yaml_load(f)

with open("example-config.yml", encoding='utf8') as ff:
    if "example-config.yml".endswith(('.yaml', '.yml')):
        openapi_ = yaml_load(ff)
    else:  # JSON file, do not transform
        openapi_ = ff


# api = API(CONFIG)


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="pygeoapi demo",
        version="0.1.0",
        routes=app.routes
    )

    # custom json file for testing
    with open("openapi.json", "r") as file:
        res = json.load(file)

    openapi_schema["info"] = res["info"]
    openapi_schema["paths"] = res["paths"]
    openapi_schema["components"] = res["components"]
    openapi_schema["servers"] = res["servers"]
    openapi_schema["tags"] = res["tags"]
    openapi_schema["openapi"] = res["openapi"]

    app.openapi_schema = openapi_schema

    return app.openapi_schema
