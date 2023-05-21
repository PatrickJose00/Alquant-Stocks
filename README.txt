I could not make the client side work on heroku.
I had an issue and did not had time to fix it in time.


Link to git: https://github.com/PatrickJose00/Alquant-Stocks

We can see the app running locally if:

    cd into client folder and run:
        - npm install
        - npm run serve

    cd into server folder and run:
        - npm install -e .
        - uvicorn main:app --reload

Links to heroku:
    - BACKEND:  https://dashboard.heroku.com/apps/stock-server-3-stocks
    - FRONTEND: https://dashboard.heroku.com/apps/stock-client-3-stocks

BACKEND is working on heroku:
    We can access data using:
        - https://stock-server-3-stocks.herokuapp.com/stocks/TSLA
        - https://stock-server-3-stocks.herokuapp.com/stocks/TSLA/statistics