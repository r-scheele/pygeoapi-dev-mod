from typing import Dict

from fastapi import APIRouter, Request
from fastapi_opa import OPAConfig
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig

router = APIRouter()


excluded_endpoints = ["/openapi.json", "/docs", "/redoc", "unprotected"]

opa_host = "http://localhost:8181"
oidc_config = OIDCConfig(
    well_known_endpoint="http://localhost:8080/auth/realms/Clients/.well-known/openid-configuration",  # noqa
    app_uri="http://localhost:8000",
    client_id="demo",
    client_secret="lbEe6bgStIi5BDGD8zPQJn7xUOfddRhC",
)
oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)


@router.get("/auth")
async def auth(request: Request):
    user_info = await oidc_auth.authenticate(request)
    return user_info


@router.get("/finance/salary/{name}")
async def salary(name: str) -> Dict:
    return {"msg": "success", "name": name}


@router.get("/unprotected")
async def profile():
    return "just me!"

