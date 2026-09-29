import json

from fastapi import HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.schemas.analysis import GoldAnalysisResponse
from app.services.gold_service import GoldService


class AnalysisService :


    def __init__(self):

        self.gold_service = GoldService()

        self.llm = ChatOpenAI(
            model=settings.OPENAI_MODEL,
            api_key= settings.OPENAI_API_KEY,
            temperature=0.2
        )

        self.structured_llm = (self.llm.with_structured_output(GoldAnalysisResponse))

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """
            You are a  GoldMarketAnalyst-AI.
            
            You are a professional precious metal market data analyst.
            Your Job is to analyze the suppplied gold market data.
            
            IMPORTANT RULES:
            1. Use ONLY the supplied market data.
            2. DO NOT invent information
            3. DO NOT use external market information. 
            4. DO NOT assume inflation, interest rates, USD Strength, geopolitical events,
            or other economics conditions unless they are explicitly provided.
            5. Do not provide personalized financial advice.
            6. Do not tell the user to buy or sell gold.
            7. Explain observable market conditions.
            8. Return minimum 3 key and maximum 5 factors .
            9. Return minimum 3 key and maximum 5 insights.
            10. Provide risks based only on the supplied data.
            11. Provide neutral market scenarios.
            12. Follow the requested structured output"""),
            ("human", """
            Here is the current gold market data : {market_data} 
            Analyze this data.""")

        ])

        self.chain = self.prompt | self.structured_llm

    async def analyze_gold(self,currency : str  = "USD") -> GoldAnalysisResponse :

        try :
            #get gold data
            gold_data = await self.gold_service.get_current_gold_price(currency)

            #Convert Pydantic object into dictionary
            market_data = gold_data.model_dump()

            response = self.chain.invoke(
                {
                "market_data" : json.dumps(market_data,indent=2)
            })

            return response
        except Exception as exc :

            raise HTTPException(status_code=500,detail="Unable to generate AI market analysis") from exc


