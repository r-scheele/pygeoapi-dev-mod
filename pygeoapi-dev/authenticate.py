import os

from fastapi import APIRouter
from fastapi_opa import OPAConfig
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig

router = APIRouter()

opa_host = "http://localhost:8181"
client_id = os.environ.get("KEYCLOAK_CLIENT_ID")
client_secret = os.environ.get("KEYCLOAK_CLIENT_SECRET")

oidc_config = OIDCConfig(
    well_known_endpoint="http://localhost:8080/auth/realms/demo/.well-known/openid-configuration",
    app_uri="http://localhost:8000/v1",
    client_id=client_id,
    client_secret=client_secret,
    get_user_info=True,
)
oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)

# list of routes that are unprotected by OIDCAuthentication
skip_endpoints = ["/test", "/docs", "redoc", "/openapi.json"]


@router.get("/test")
async def test():
    return {"message": "works without login because it is not protected with OIDCAuthentication"}
