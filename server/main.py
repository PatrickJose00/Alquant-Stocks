from fastapi import FastAPI
from app.api.endpoints import stocks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI(debug=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# Include the routers for your API
app.include_router(stocks.router)



# Run the app with Uvicorn
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)