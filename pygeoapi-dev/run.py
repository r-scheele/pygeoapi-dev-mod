import uvicorn

from utils import CONFIG

if __name__ == '__main__':
    host = CONFIG["server"]["bind"]["host"]
    port = CONFIG["server"]["bind"]["port"]
    uvicorn.run("main:app", host=host, port=port, reload=True)
