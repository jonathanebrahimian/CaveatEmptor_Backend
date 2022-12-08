from fastapi import APIRouter

from app.database import report_collection,stats_collection
from app.routes.report import call_lambda
router = APIRouter()
TOKENS = ['0xdAC17F958D2ee523a2206206994597C13D831ec7','0xB8c77482e45F1F44dE1745F52C74426C631bDD52','0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
            '0x4Fabb145d64652a948d72533023f6E7A623C7C53','0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0','0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84',
            '0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE','0x3883f5e181fccaF8410FA61e12b59BAd963fb645','0x75231F58b43240C9718Dd58B4967c5114342a86c',
            '0x6B175474E89094C44Da98b954EedeAC495271d0F']

@router.get("/", response_description="Get analysis")
async def algo_update():
    report_collection.delete_many({})
    stats_collection.delete_many({})
    for token in TOKENS:
        call_lambda(token)
    return True




