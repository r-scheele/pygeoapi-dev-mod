FROM authorizon/opal-client:latest
RUN export PATH=$PATH:$HOME/.poetry/bin
RUN poetry install --user opal-fetcher-postgres
