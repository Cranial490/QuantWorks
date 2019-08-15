import pandas as pd
import Utilities, Globals

class technical_indicators(self):
	def sma(self, interval):
		df = Globals.data_frame
		df.reset_index(level=0, inplace=True)
		df.columns = ['ds', 'y']
		return df.y.rolling(window=interval).mean()

	def ema(self, interval):
		df = Globals.data_frame
		df.reset_index(level=0, inplace=True)
		df.columns = ['ds', 'y']
		return df.y.ewm(span=interval, min_periods=interval, adjust=False).mean()
		
	def ema_ema(self, interval):
		df = Globals.data_frame
		return ema(ema(df, interval), interval)

	def dema(self, interval):
		df = Globals.data_frame
		return 2*ema(df, interval) - ema_ema(df, interval)

	def rsi(self, interval):
		df = Globals.data_frame
		df.reset_index(level=0, inplace=True)
		df.columns = ['ds', 'y']
		gain = 0, loss = 0
		current_ltp = df['y'].iloc[-1]
		if current_ltp > df['y'].iloc[-2]:
			f = 1
			gain = current_ltp - df['y'].iloc[-2]
		else:
			f = 0
			loss = df['y'].iloc[-2] - current_ltp
		df = df[-14:-1]
		avg_gain = 0.0
		avg_loss = 0.0
		row_iterator = df.iterrows()
		_, last = row_iterator.next()
		for i, row in row_iterator:
			if not pd.isna(last['y']):
				if last['y'] - row['y'] > 0.0:
					first_avg_gain += last['y'] - row['y']
				else:
					first_avg_loss += row['y'] - last['y']
		avg_gain = (first_avg_gain*13 + f*gain) / 14
		avg_loss = (first_avg_loss*13 + f*loss) / 14
		RS = avg_gain / avg_loss
		RSI = 100 - 100 / (1 + RS)
		return RSI

	def atr(self, ohlc, interval):
		cf = Globals.candles_dataframe
		token = cf['token'].iloc[-1]
		current_open = cf['open'].iloc[-1]
		current_high = cf['high'].iloc[-1]
		current_low = cf['low'].iloc[-1]
		current_close = cf['close'].iloc[-1]
		true_range = 0.0
		cf = cf[-14:-1] # last 14 5-minute candles except the last one
		row_iterator = cf.iterrows()
		_, last = row_iterator.next()
		for i, row in row_iterator:
			if not pd.isna(last['close']):
				true_range += max(abs(last['high'] - row['close']), abs(last['low'] - row['close']), abs(last['high'] - last['low']))
		average_true_range = true_range / 14.0
		current_atr = max(abs(current_high - cf['close'].iloc[-1]), abs(current_low - cf['close'].iloc[-1]), abs(current_high - current_low))
		average_true_range = (average_true_range * 13 + current_atr) / 14.0
		return average_true_range



	def vwap(self):
		df = Globals.data_frame
		total_price = 0.0
		total_volume = 0.0
		for index, row in df.iterrows():
			total_price += row[LTP]*row[Volume]
			total_volume += row[Volume]
		if total_volume == 0.0:
			return 1.0
		else:
			return total_price / total_volume
		




