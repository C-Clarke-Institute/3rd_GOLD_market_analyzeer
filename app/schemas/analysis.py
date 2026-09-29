from typing import List

from pydantic import BaseModel, Field


class MarketFactor(BaseModel):

    factor : str = Field(description="The Market Factor affecting gold")
    impact : str = Field(description="How the factor relates to thee supplied data")
    explanation : str = Field(description="Short explanation based only on supplied data")

class MarketInsight(BaseModel):
    title : str
    explanation : str

class MarketScenario(BaseModel):

    scenario : str
    description : str

class GoldAnalysisResponse(BaseModel):

    symbol : str
    market_summary : str
    key_factors : List[MarketFactor] = Field(min_length=3, max_length=5)
    insights : List[MarketInsight]= Field(min_length=3,max_length=5)
    risks : List[str]
    scenarios : List[MarketScenario]
    date_timestamp : int | None = None