from fastapi import APIRouter
from app.services import stock_services
from typing import List

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"],
)

@router.get("/{symbol}")
async def get_stock_data(symbol: str):
    try:
        data = await stock_services.get_stock_data_with_values_adjusted(symbol)
        return {"symbol": symbol, "data": data}
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {"symbol": None, "data": None}  # Return empty value or a default response

@router.get("/{symbol}/statistics")
async def get_stock_statistics(symbol: str):
    try:
        data = await stock_services.get_stock_data_with_values_adjusted(symbol)
        if data:
            statistics = await stock_services.calculate_statistics(data, symbol)
            return {"statistics": statistics}
        else:
            return {"statistics": None}  # Return empty value or a default response
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {"statistics": None}  # Return empty value or a default response

