import pandas as pd


def init():
    global data_frame, df_cols, tick_df, candles_dataframe
    global trd_portfolio
    trd_portfolio = {895745: "TATASTEEL"}
    df_cols = ["Token", "LTP", "Volume"]
	data_frame = pd.DataFrame(data=[],columns=df_cols, index=[])
	tick_df = pd.DataFrame(data.values(), columns=df_cols, index=data.keys()) #convert data to a DataFrame
	history_data_frame = pd.DataFrame(data=[], columns=df_cols, index=[])
	candles_cols = ["Token", "Open", "High", "Low", "Close"]
	candles_dataframe = pd.DataFrame(data=[], columns=df_cols, index=[])