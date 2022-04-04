# from authx import JWTBackend, RedisBackend
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from starlette.config import Config

config = Config(".env")

# SecurityConfig = JWTBackend(
#     cache_backend=RedisBackend,
#     private_key=config("PRIVATE_KEY", default="private_key"),
#     public_key=config("PUBLIC_KEY", default="public_key"),
#     access_expiration=3600,
#     refresh_expiration=3600
# )

oauth_token_scheme = HTTPBearer()
router = APIRouter()


# Set Anonymous User
@router.get("/anonym")
def anonym_test():
    pass


# Set Authenticated User
@router.get("/user")
async def user_test(token=Depends(oauth_token_scheme)):
    # is_verified = await SecurityConfig.decode_token(token)
    # print(is_verified)
    pass
