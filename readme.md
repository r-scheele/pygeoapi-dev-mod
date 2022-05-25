
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
   export PYGEOAPI_CONFIG=example-config.yml && export PYGEOAPI_OPENAPI=example-openapi.yml
   ```

6. run the server
   ```sh
   python3 pygeoapi-dev/run.py
   ```


## Usage

Few containers are needed to run the server.

### 1. Keycloak 
Intall keycloak on Linux with the following commands:

```sh
docker run -d -p 8080:8080 -e KEYCLOAK_USER='admin' -e KEYCLOAK_PASSWORD='admin' jboss/keycloak:latest

```

Intall keycloak on Mac M1 with the following commands:

   
   ```sh
docker run -d -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin wizzn/keycloak:14

   ```


### 2. Build the Postgres-data-fetcher image
   
   ```sh
docker build -t pygeoapi-dev/opal-client -f ./Dockerfile .   
```

### 3. Run the other containers
   
   ```sh
   docker-compose up -d
   ```
