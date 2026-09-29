import httpx

from app.core.config import settings


class GoldAPIClient:

    def __init__(self):

        self.base_url = settings.GOLD_API_BASE_URL

        self.headers = {
            "x-access-token" : settings.GOLD_API_KEY,
            "Content-Type" : "application/json"
        }

    async def get_gold_price(self,symbol: str = "XAU", currency : str = "USD"):

        url = f"{self.base_url}/{symbol}/{currency}"

        async with httpx.AsyncClient(timeout=10.0) as client :
            response = await client.get(url, headers=self.headers)

        response.raise_for_status()

        return response.json()