from typing import Dict

from fastapi import APIRouter, Request
from fastapi_opa import OPAConfig
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig

router = APIRouter()


opa_host = "http://localhost:8181"
oidc_config = OIDCConfig(
    well_known_endpoint="http://localhost:8080/auth/realms/demo/.well-known/openid-configuration",  # noqa
    app_uri="http://localhost:8000",
    client_id="demo",
    client_secret="q5NcHAH3AinTNDb77iJ6k76mOqNPEGfw", get_user_info=True,
)
oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)


@router.get("/finance/salary/{name}")
async def salary(name: str) -> Dict:
    return {"msg": "success", "name": name}


