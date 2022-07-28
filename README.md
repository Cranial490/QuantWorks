# QuantWorks
Python wrapper for [kite API](https://kite.trade/docs/connect/v3/) to test trading strategies in live market and also deploy them live. This framework makes it easier to communicate with Kite Connect API.<br>
[Kite Connect](https://github.com/zerodha/pykiteconnect/blob/master) gives their users direct access to the Indian stock market and makes executing orders using python script in real time accessible. One of the main concern with the API is complex the login flow which we automate.  

### Login
We make use of Selenium to fetch access token from kite.<br>
- First you need to download webdriver for your browser for Selenium. [Here](https://chromedriver.chromium.org/downloads) is the link for chrome webdriver.
- Login process makes use of `config.properties` file to fetch the user details such as `api_key` and `api_secret` to access the API. You can generate your own config.properties file using the `config.py`. Make sure you **dont share** the `config.properties` file publicly as it contains accounts sensitive information. Give the path to the webdriver in `cofig.py`.
- Now you can run `setup.py` which will fetch the access token and setup a kiteInstance which connects you to the API.

### Backtesting
- To start backtesting you need to fetch historical data for your intrument. For this use `DataFetch.py`.
- You need to provide your config.properties path, path where you will store data and the start date and end date for historical data.
- Run `DataFetch.py` along with the instrument number and you will get the csv's created with your data.
- To start backtesting with this data you can put your strategy in `backTest.py` and start teting.
- You can use methods in `positionManaget.py` to backtest.

### Live Ticks
- To connect with market and get live ticks for your intrument use `LiveTicks.py`.


### Kite important links
------ 

* [Tick data to dataframes](https://kite.trade/forum/discussion/2552/issue-data-from-websocket-to-python-dataframes)

* [Volume calculation for each interval of a particular time frame](https://kite.trade/forum/discussion/5569/volume-calculation)

* [Ways to get pre-market data (in json format)](https://kite.trade/forum/discussion/comment/21056/#Comment_21056)

* [Downloading historical data](https://kite.trade/forum/discussion/comment/21057/#Comment_21057)

* [Converting ticks to candle](https://kite.trade/forum/discussion/2604/convert-ticks-to-candle)

* [Stoploss order placement](https://github.com/Aprataksh/Munafa/blob/78e73c18103a5c193a65e0c130f00bf25e66f9d9/Zerodha/utilites/stoploss%20order%20placement.py)

* [Order state transitions (OnOrderUpdate)](https://kite.trade/forum/discussion/comment/20023/#Comment_20023)

* [How to know the status of order](https://kite.trade/forum/discussion/2749/how-to-find-the-status-of-an-order)

* [CO leverage calculator](https://zerodha.com/z-connect/tradezerodha/zerodha-trader-software-version/cover-orders-for-higher-leverage)

* [BO leverage calculator](https://zerodha.com/margin-calculator/BracketCover/)

* [Equity margin calculator](https://zerodha.com/margin-calculator/Equity/)

* [Commodities margin calculator](https://zerodha.com/margin-calculator/Commodity/)

------
*There is a lot if work needed to be done on this framework, feel free to contribute or use as you wish*


