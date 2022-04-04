import os
from pathlib import Path

import uvicorn

app_path = Path(os.path.join(os.path.dirname(__file__)))
if __name__ == '__main__':
    from pygeoapi.util import yaml_load
    if "PYGEOAPI_CONFIG" not in os.environ:
        raise RuntimeError("PYGEOAPI_CONFIG environment variable not set")
    config_path = os.path.join(app_path, os.environ.get("PYGEOAPI_CONFIG"))
    with open(config_path, encoding="utf-8") as f:
        CONFIG = yaml_load(f)

    host = CONFIG["server"]["bind"]["host"]
    port = CONFIG["server"]["bind"]["port"]

    uvicorn.run("main:app", host=host, port=port, reload=True)
