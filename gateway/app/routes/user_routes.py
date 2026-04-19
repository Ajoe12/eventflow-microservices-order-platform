from fastapi import APIRouter, Request
from app.services.proxy_service import proxy_request
from app.core.config import USER_SERVICE_URL

router = APIRouter(prefix="/users", tags=["Users"])

@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_user(request: Request, path: str):
    print(path,str(request),USER_SERVICE_URL)
    return await proxy_request(
        request,
        base_url=USER_SERVICE_URL,
        path=f"/{path}"
    )