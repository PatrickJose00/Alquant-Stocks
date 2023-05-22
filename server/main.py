from fastapi import FastAPI
from app.api.endpoints import stocks
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

app.include_router(stocks.router)

# Run the app with Uvicorn
if __name__ == "__main__":

   icorn.run(app, host="https://stock-server-3-stocks.herokuapp.com", port=8000)