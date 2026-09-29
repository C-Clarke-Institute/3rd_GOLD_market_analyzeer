from fastapi import HTTPException

from app.clients.gold_api import GoldAPIClient
from app.schemas.gold_schemas import GoldPriceResponse, GoldStatisticsResponse


class GoldService :

    def __init__(self):

        self.client = GoldAPIClient()

    async def get_current_gold_price(self,currency : str = "USD") -> GoldPriceResponse:

        try:

            data = await self.client.get_gold_price(symbol="XAU",currency=currency.upper())

        except Exception as exc :
            raise HTTPException(status_code = 200,detail="Unable to retrieve gold market data" ) from  exc

        return GoldPriceResponse(
            symbol="XAU",
            currency=currency.upper(),
            price=data["price"],
            price_gram_24k=data.get("price_gram_24k"),
            change=data.get("ch"),
            change_percent=data.get("chp"),
            open_price=data.get("open_price"),
            high_price=data.get("high_price"),
            low_price=data.get("low_price"),
            previous_close=data.get("prev_close_price"),
            timestamp = data.get("timestamp")

        )

    async def get_statistics(self,currency : str = "USD" ) -> GoldStatisticsResponse:

        gold = await self.get_current_gold_price(currency)
        price_range = None

        if gold.high_price is not None and gold.low_price is not None :
            price_range = gold.high_price - gold.low_price

        return GoldStatisticsResponse(
            symbol= gold.symbol,
            currency= gold.currency,
            current_price= gold.price,
            high_price= gold.high_price,
            low_price= gold.low_price,
            open_price= gold.open_price,
            previous_price = gold.previous_close,
            change= gold.change,
            change_percent= gold.change_percent,
            price_range= price_range

        )