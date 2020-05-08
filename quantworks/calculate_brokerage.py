import csv, sys

# once the order is placed and "complete" calculate the brokerage and subtract it from the PnL and show it to the user 
# if required

# net pnl for commodities = num_of_lots*fabs(entry-exit)*pnl_for_1_rupee
net_pnl = 0.0 # pnl for the day
capital = 100000.0 # total trading capital in the account #should be less than 1 billion rupees
NON_AGRI = ['ALUMINI','ALUMINIUM','BRENTCRUDE','COPPER','COPPERM','CRUDEOIL','CRUDEOILM','GOLD','GOLDGUINEA','GOLDM','GOLD GLOBAL','GOLDPETAL','GOLDPTLDEL','LEAD','LEADMINI','NATURALGAS','NICKEL','NICKELM','SILVER','SILVER1000','SILVERM','SILVERMIC','ZINC','ZINCMINI'] # use the below link to populate the list
AGRI = ['CARDAMOM', 'COTTON', 'CPO', 'KAPAS', 'MENTHAOIL'] 
COMMODITY_MARGIN = dict() # key = tradingsymbol, value = {MIS_MARGIN:, pnl_for_1_rupee:}
EQ_MARGIN = dict() # key = tradingsymbol, value = EQUITY_MARGIN

'''
- 'initialize_dict()' - initialises the Commodities margin dictionary
- 'equity_margin()' - stores the margin of the equity stocks in a dictionary whose key is the trading symbol and value is 
the margin provided.
- 'commodities_margin()' - stores the MIS_MARGIN as well as the Pnl per rupee in a dictionary for the Commodities listed 
in "MCX" 
- 'margin_calculator()' - returns the maximum number of stocks that can be traded for each kind of order given the 
available capital and leverage
- 'brokerage_calculator()' - returns the brokerage after the order status is "COMPLETE" for all the instruments traded 
in "NSE" and "MCX"
'''


class Model:

	def equity_margin(self):
		with open('../resources/equity_margin.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count=0
			for row in csv_reader:
				if line_count == 0:
					pass
				else:
					stock = row[0]
					margin = row[1].rsplit('x')[0]
					if margin.isdigit():
						EQ_MARGIN[stock] = float(margin)
					#print(stock, margin)
				line_count += 1
	# can be a part of util class

	def initialize_dict(self):
		for stock in NON_AGRI:
			COMMODITY_MARGIN[stock]={'pnl_per_rupee':0.0, 'MIS_MARGIN':0.0}
		for stock in AGRI:
			COMMODITY_MARGIN[stock]={'pnl_per_rupee':0.0, 'MIS_MARGIN':0.0}


	def commodities_margin(self):
		#initialize_dict()
		#print(COMMODITY_MARGIN)
		with open('../resources/pnl_for_1_rupee_commodities.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count=0
			for row in csv_reader:
				if line_count == 0:
					pass
				else:
					stock = row[0]
					pnl_per_rupee = row[2]
					if(pnl_per_rupee.isdigit()):
						COMMODITY_MARGIN[stock]['pnl_per_rupee'] = float(pnl_per_rupee)
					#print(stock, margin)
				line_count += 1
		with open('../resources/MIS_MARGIN_COMMODITIES.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count=0
			for row in csv_reader:
				if line_count == 0:
					pass
				else:
					stock = row[0]
					MIS_MARGIN = row[4]
					if(MIS_MARGIN != "0"):
						COMMODITY_MARGIN[stock]['MIS_MARGIN'] = float(MIS_MARGIN)
					else:
						COMMODITY_MARGIN[stock]['MIS_MARGIN'] = 1000000000.0
					#print(stock, margin)
				line_count += 1
	'''
	def order_history(self, order_id):
	        """
	        Get history of individual order.
	        - `order_id` is the ID of the order to retrieve order history.
	        """
		return self._format_response(self._get("order.info", {"order_id": order_id}))
	'''

	'''
	def order():
		#place_order
		if(OnOrderUpdate()):
			if(status='COMPLETE' && pending_quantity == 0):
				if transaction_type == 'buy':
					flag=-1
				else: 
					flag=1
				net_pnl = flag*(average_price - price)-calculate_brokerage(average_price, price, filled_quantity, flag, exchange, tradingsymbol)
				# assuming Limit order only 
	'''

	def margin_calculator(self, exchange, tradingsymbol, variety, ltp): # variety - BO/CO/regular/AMO, also can send the order ID for ltp
		# margin calculation for BO/CO  - https://zerodha.com/margin-calculator/BracketCover/
		# for BO/CO margin = min(SL * num_of_stocks, 0.025*entry)
		# margin calculation for equity (Regular order) - EQ_MARGIN[stock]
		# for regular order margin, store the margins in a dict()
		# margin calculation for commodities - https://zerodha.com/margin-calculator/Commodity/
		# MIS margins from the list
		num_of_stocks = 0
		if exchange == 'NSE':
			margin = EQ_MARGIN.get(tradingsymbol, 1.0)
			#num_of_stocks = margin / tradingsymbol[ltp] # margin divided by last traded price of the trading symbol
			num_of_stocks = (capital * margin) / ltp

		else:
			if capital > COMMODITY_MARGIN[tradingsymbol]['MIS_MARGIN']:
				num_of_stocks = int(capital / COMMODITY_MARGIN[tradingsymbol]['MIS_MARGIN'])
		return int(num_of_stocks)

		# return num_of_stocks that can be bought according to risk management and leverage provided



	def brokerage_calculator(self, exit, entry, num_of_stocks, transaction_type, exchange, tradingsymbol):
		# instead of passing all these as arguments, call order_history and retrieve the values of the latest order
		if exchange == 'NSE':
			Brokerage = min(0.0001*num_of_stocks*(entry+exit), 40)
			STT = 0.00025*num_of_stocks*exit#(entry if transaction_type == -1 else exit)
			Transaction_charges = num_of_stocks*(entry+exit)*0.0000325
			Service_Tax = 0.18*(Brokerage + Transaction_charges)
			Education_Cess = 0.02*Service_Tax
			Higher_Education_Cess = 0.01*Service_Tax
			SEBI_Charges = num_of_stocks*(entry+exit)/1000000.0
			Stamp_charges = 0.00003*num_of_stocks*(entry+exit)

		elif exchange == 'MCX':
			max_num_of_lots = capital / COMMODITY_MARGIN[tradingsymbol]['MIS_MARGIN']
			num_of_stocks = num_of_stocks*COMMODITY_MARGIN[tradingsymbol]['pnl_per_rupee']
			Brokerage = min(0.0001*num_of_stocks*(entry+exit), 40)
			STT = (0.0001*num_of_stocks*exit)# if tradingsymbol in NON_AGRI else 0.0
			Transaction_charges = num_of_stocks*(entry+exit)*0.000026 # (0.000031 if tradingsymbol in NON_AGRI else 0.0000175) 
			Service_Tax = 0.18*(Brokerage + Transaction_charges)
			Education_Cess = 0.02*Service_Tax
			Higher_Education_Cess = 0.01*Service_Tax
			SEBI_Charges = num_of_stocks*(entry+exit)/1000000.0
			Stamp_charges = 0.00003*num_of_stocks*(entry+exit)
		print(Brokerage, STT, Transaction_charges, Service_Tax, Education_Cess, Higher_Education_Cess, SEBI_Charges, Stamp_charges)
		return (Brokerage + STT + Transaction_charges + Service_Tax + SEBI_Charges + Stamp_charges) # + Education_Cess + Higher_Education_Cess
		# education cess and higher education cess not added in the brokerage calculator



obj = Model()
obj.equity_margin()
obj.initialize_dict()
print(EQ_MARGIN)
print(obj.margin_calculator('NSE', 'AARTIDRUGS', 'BO', 2098))
print(obj.margin_calculator('NSE', 'YESBANK', 'BO', 1000))
obj.commodities_margin()
print(COMMODITY_MARGIN['CRUDEOIL']['pnl_per_rupee'])
print(COMMODITY_MARGIN['COPPER']['MIS_MARGIN'])
print(COMMODITY_MARGIN['NATURALGAS'])
print(COMMODITY_MARGIN['MENTHAOIL'])
print(COMMODITY_MARGIN)
print(obj.margin_calculator('MCX', 'CRUDEOIL', 'regular', 1800))

'''
#print(EQ_MARGIN)
obj.commodities_margin()
#print(COMMODITY_MARGIN)
#print(COMMODITY_MARGIN['COTTON']['pnl_per_rupee'])
print(obj.brokerage_calculator(4327, 4322, 3, 1, 'MCX', 'CRUDEOILM'))
#print(margin_calculator('NSE', 'ACC', 'BO'))
'''


