import Globals
import pandas as pd

class Utilities:

    def write_to_database(self):
        pass
        #takes a dictionary or a dataframe as input and writes it to an output file.

    def ticks_to_candle(self, tick, interval, ohlc):
    	try:
    		if tick['timestamp'].minute%interval == 0 and ohlc[tick['instrument_token']][4]:
    			#print(trd_portfolio[tick['instrument_token']]," : ",ohlc[tick['instrument_token']][0]," : ",ohlc[tick['instrument_token']][1]," : ",ohlc[tick['instrument_token']][2]," : ",ohlc[tick['instrument_token']][3]) #printing last candle
    			candle = pd.DataFrame(data.values(), columns=Globals.df_cols, index=data.keys())
    			token = Globals.trd_portfolio[tick['instrument_token']]
    			open = ohlc[tick['instrument_token']][0]
    			high = ohlc[tick['instrument_token']][1]
    			low = ohlc[tick['instrument_token']][2]
    			close = ohlc[tick['instrument_token']][3]
    			data[token] = [open, high, low, close]
    			#if(len(Globals.candles_dataframe) == 0):
				Globals.candles_dataframe.append(Globals.tick_df)
				#else:
				#	Globals.candles_dataframe = Globals.candles_dataframe.append(Globals.tick_df) # append to existing
    			
    			ohlc[tick['instrument_token']][4] = False

    			# making ohlc for new candle
    			ohlc[tick['instrument_token']][0] = tick['last_price']; #open
				ohlc[tick['instrument_token']][1] = tick['last_price']; #high
				ohlc[tick['instrument_token']][2] = tick['last_price']; #low
				ohlc[tick['instrument_token']][3] = tick['last_price']; #close


				ohlc[tick['instrument_token']][5] = tick['timestamp'].minute+1

			# calculating high, low and close price

			if ohlc[tick['instrument_token']][1] < tick['last_price']: #calculating high
				ohlc[tick['instrument_token']][1] = tick['last_price']

			if ohlc[tick['instrument_token']][2] > tick['last_price'] or ohlc[tick['instrument_token']][2] == 0: #calculating low
				ohlc[tick['instrument_token']][2] = tick['last_price']

			ohlc[tick['instrument_token']][3] = tick['last_price'] #closing price

			if tick['timestamp'].minute%ohlc[tick['instrument_token']][5] == 0:
				ohlc[tick['instrument_token']][4] = True;
		
		except Exception as e:
			print(e);

		return ohlc