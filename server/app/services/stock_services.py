import os
import httpx
import os
from dotenv import load_dotenv
from app.utils import stock_utils

load_dotenv()

async def get_stock_data(symbol: str):
    try:
        # Set up Alpha Vantage API parameters
        api_key = os.getenv("ALPHA_API_KEY")
        base_url = "https://www.alphavantage.co/query"
        function = "TIME_SERIES_INTRADAY"
        interval = "5min"  # Use "full" for complete data (limited in free tier)

        # Make request to Alpha Vantage API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                base_url,
                params={
                    "function": function,
                    "symbol": symbol,
                    "interval": interval,
                    "apikey": api_key,
                },
            )
            response.raise_for_status()

            # Extract stock data from response
            data = response.json()["Time Series (5min)"]

            # Transform data into desired format
            stock_data = []
            for timestamp, values in data.items():
                value = float(values["4. close"])
                rounded_value = round(value, 2)  # Format value to two decimal places
                stock_data.append({"timestamp": timestamp, "value": rounded_value})

            return stock_data

    except (httpx.HTTPError, KeyError) as e:
        return {"message": "Error occurred while fetching stock data."}


async def get_stock_data_with_values_adjusted(symbol: str):
    stock_data = await get_stock_data(symbol)
    if stock_data:
        first_values = [stock["value"] for stock in stock_data]
        adjustment_factor = 100 - first_values[0]
        for stock in stock_data:
            stock["value"] += adjustment_factor
        return stock_data



async def calculate_statistics(data, symbol):
    statistics = {}

    cumulative_return = stock_utils.calculate_cumulative_return(data)
    annualized_return = stock_utils.calculate_annualized_return(data)
    annualized_volatility = stock_utils.calculate_annualized_volatility(data)
        
    statistics[symbol] = {
        "cumulative_return": cumulative_return,
        "annualized_return": annualized_return,
        "annualized_volatility": annualized_volatility
        }
    return statistics

