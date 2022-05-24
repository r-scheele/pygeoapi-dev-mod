
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/r-scheele/pygeoapi-dev-mod.git
   ```
2. change to project directory and activate virtual environment
   ```sh
   cd pygeoapi-dev-mod && poetry shell
   ```

3. Install gdal
### For MacOS
```sh
   brew install gdal
   ```


4. Install dependencies
   ```sh
   poetry install
   ```

5. Set environment variables in `example-config.yml`
   ```sh
   export PYGEOAPI_CONFIG=example-config.yml
   ```

6. run the server
   ```sh
   python3 pygeoapi-dev/run.py
   ```

