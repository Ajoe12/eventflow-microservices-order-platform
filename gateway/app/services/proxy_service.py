from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.http_client import forward_request


async def proxy_request(request: Request, base_url: str, path: str):
    # 🔹 Build target URL
    url = f"{base_url}{path}"

    # 🔹 Extract method
    method = request.method

    # 🔹 Copy headers
    headers = dict(request.headers)

    # 🔥 Remove problematic headers
    headers.pop("content-length", None)
    headers.pop("host", None)
    headers.pop("connection", None)

    # 🔹 Query params
    params = dict(request.query_params)

    # 🔹 Raw body (IMPORTANT)
    body = await request.body()

    # 🔹 Forward request
    response = await forward_request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        content=body
    )

    # 🔥 Return proper response (status + body)
    try:
        data = response.json()
    except Exception:
        data = response.text

    return JSONResponse(
        content=data,
        status_code=response.status_code
    )