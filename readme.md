
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/r-scheele/pygeoapi-dev-mod.git
   ```
2. activate the virtual environment - make sure poetry is added to PATH
   ```sh
   poetry shell
   ```
3. Install dependencies
   ```sh
   cd pygeoapi-dev-mod && poetry install
   ```
4. Set environment variables in`example-config.yml`
   ```sh
   export PYGEOAPI_CONFIG=example-config.yml
   ```

5. run the server
   ```sh
   python3 pygeoapi-dev/run.py
   ```

