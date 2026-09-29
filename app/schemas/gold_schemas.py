from typing import Optional

from pydantic import BaseModel


class GoldPriceResponse(BaseModel):

    symbol : str
    currency : str
    price : float
    price_gram_24k : Optional[float] = None
    change: Optional[float] = None
    change_percent : Optional[float] = None

    open_price : Optional[float] = None
    high_price : Optional[float] = None
    low_price : Optional[float] = None
    previous_close : Optional[float] = None

    timestamp = Optional[int] = None


class GoldStatisticsResponse(BaseModel):

    symbol : str
    currency : str
    current_price : float
    high_price : Optional[float] = None
    low_price : Optional[float] = None
    open_price : Optional[float] = None
    previous_close : Optional[float] = None

    change : Optional[float] = None
    change_percent : Optional[float] = None
    price_range : Optional[float] = None

