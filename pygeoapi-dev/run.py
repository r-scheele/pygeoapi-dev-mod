import os

import uvicorn
if __name__ == '__main__':
    from pygeoapi.util import yaml_load
    if "PYGEOAPI_CONFIG" not in os.environ:
        raise RuntimeError("PYGEOAPI_CONFIG environment variable not set")
    with open(os.environ.get("PYGEOAPI_CONFIG"), encoding="utf-8") as f:
        CONFIG = yaml_load(f)

    host = CONFIG["server"]["bind"]["host"]
    port = CONFIG["server"]["bind"]["port"]

    uvicorn.run("main:app", host=host, port=port, reload=True)
