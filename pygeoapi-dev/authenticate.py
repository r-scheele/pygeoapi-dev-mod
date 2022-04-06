from authx import JWTBackend, RedisCacheBackend
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

SecurityConfig = JWTBackend(
    cache_backend=RedisCacheBackend(host='localhost', port=6379),
    private_key=("private_key"),
    public_key=("public_key"),
    access_token_expiration=3600,
    refresh_token_expiration=3600
)


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/potected")
async def get_potected(token = Depends(oauth2_scheme)):
    pass
