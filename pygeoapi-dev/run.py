import uvicorn
import os
from utils import CONFIG

print(os.environ)
if __name__ == '__main__':
    host = CONFIG["server"]["bind"]["host"]
    port = CONFIG["server"]["bind"]["port"]
    uvicorn.run("main:app", host=host, port=port, reload=True)
