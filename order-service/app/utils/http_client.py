import httpx

async def get_item(item_id: str, base_url: str,token:str):
    print(base_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{base_url}/items/{item_id}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        if response.status_code != 200:
            return None

        return response.json()