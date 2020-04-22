from kiteconnect import KiteConnect

api_key = ""
access_token = ""


instrument_token = ""

from_date = ""
to_date = ""

interval = ""

kite = KiteConnect(api_key=api_key)

try:
	kite.set_access_token(access_token)
except Exception, e:
	print e,"Error while setting access token"


#fetching historical data
def get_historical_records():
	try:
		return kite.historical(instrument_token,from_date,to_date,interval)
	except Exception, e:
		print e



def strategy(records):
	total_closing_price = 0
	record_count = 0
	order_placed = False
	last_order_placed = None
	last_order_price = 0
	profit = 0

	for record in records:
		record_count += 1
		total_closing_price += record["close"]

		#moving average is calculated for every 5 ticks
		if record_count >= 5:
			moving_average = total_closing_price/5 # use lib to calculate moving average

			#if moving average greater than the last tick, place a buy order
			if record["close"] > moving_average:
				if last_order_placed == "SELL" or last_order_placed is None:
					if last_order_placed == "SELL":
						print "Exit SELL"

						profit += last_order_price - record["close"]
						last_order_price = record["close"]

					#place fresh buy order
					print "place new BUY order"
					last_order_placed == "BUY"					
			#if moving average is lesser than the tick, and there is a position, place order
		elif record["close"] < moving_average:
			if last_order_placed == "BUY"
				# as last order was buy first exit the position
				print "Exit BUY"

				#Calculate profit
				profit += record["close"] - last_order_price
				last_order_price = record["close"]

				#Fresh sell order
				print "place new sell order"

		total_closing_price -= records[record_count-5]["close"]
	print "Gross profit ", profit

	place_order(last_order_placed)

#Place order based on transaction type(Buy/Sell)
def place_order(transaction_type):
	order_id = kite.order_place(tradingsymbol="RELIANCE", exchange="NSE", quantity=1, transaction_type=transaction_type, order_type="MARKET",product="CNC")
	response = kite.get_order(order_id)
	if "rejected" in response["status"]:
		#perform action


def start():
	records = get_historical_records()
	strategy(records)
