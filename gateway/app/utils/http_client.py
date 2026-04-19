import httpx


async def forward_request(
    method: str,
    url: str,
    headers: dict,
    params: dict = None,
    content: bytes = None
):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            content=content   # 🔥 raw body (not json)
        )

    return response