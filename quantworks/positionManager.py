def update_quantity(positions, ticker, price, quantity, transaction_type):
    if transaction_type == 'BUY':
        return positions[ticker]['Qty'] + abs(quantity) # added abs akshay
    else:
        return positions[ticker]['Qty'] - abs(quantity) # added abs akshay


def calculate_avg_price(positions, ticker, price, quantity, transaction_type):
    if ((positions[ticker]['Qty'] > 0 and transaction_type == 'BUY') or (positions[ticker]['Qty'] < 0 and transaction_type == 'SELL')):
        return (positions[ticker]['AvgPrice'] * abs(positions[ticker]['Qty']) + price * quantity) / (abs(positions[ticker]['Qty']) + quantity)
    # added by akshay
    elif (positions[ticker]['Qty'] == 0):
        return price
    ##################
    else:
        return positions[ticker]['AvgPrice']


def calculate_realized_PnL(positions, ticker, price, quantity, transaction_type):
    if ((positions[ticker]['Qty'] > 0 and transaction_type == 'SELL') or (positions[ticker]['Qty'] < 0 and transaction_type == 'BUY')):
        # Written by akshay
        if(positions[ticker]['Qty'] < 0):
            if(quantity>0):
                return positions[ticker]['realized_PnL'] + (positions[ticker]['AvgPrice'] - price) * quantity
            else:
                return positions[ticker]['realized_PnL'] + (price - positions[ticker]['AvgPrice']) * quantity
        elif(positions[ticker]['Qty'] > 0):
            if (quantity>0):
                return positions[ticker]['realized_PnL'] + (price - positions[ticker]['AvgPrice']) * quantity
            else:
                return positions[ticker]['realized_PnL'] + (positions[ticker]['AvgPrice'] - price) * quantity

        # Written by Pranjal
        '''
        if positions[ticker]['Qty'] > 0:
            return positions[ticker]['realized_PnL'] + (price - positions[ticker]['AvgPrice']) * quantity
        elif positions[ticker]['Qty'] < 0:
            return positions[ticker]['realized_PnL'] + (positions[ticker]['AvgPrice'] - price) * quantity
        '''
    else:
        return positions[ticker]['realized_PnL']


def calculate_pnl(positions, ticker, price, quantity):
    return (positions[ticker]['realized_PnL'] + (positions[ticker]['LTP'] - positions[ticker]['AvgPrice']) * positions[ticker]['Qty'])

def update_ltp(positions, ticker, price):
    positions[ticker]['LTP'] = price

def update_positions(positions, ticker, price, quantity, transaction_type):
    if quantity != 0:
        if ticker not in positions:
            if(transaction_type == 'SELL'):
                quantity = quantity * (-1)
            positions[ticker] = {'Qty': quantity, 'AvgPrice': price,'LTP': price, 'CurrValue': abs(quantity * price), 'P&L': 0, 'realized_PnL': 0}

        elif ticker in positions: #quantity= (-5)
            positions[ticker]['AvgPrice'] = calculate_avg_price(positions=positions, ticker=ticker, price=price, quantity=quantity, transaction_type=transaction_type)

            positions[ticker]['LTP'] = price

            positions[ticker]['realized_PnL'] = calculate_realized_PnL(positions=positions, ticker=ticker, price=price, quantity=quantity, transaction_type=transaction_type)

            positions[ticker]['Qty'] = update_quantity(positions=positions, ticker=ticker, price=price, quantity=quantity, transaction_type=transaction_type)

            positions[ticker]['P&L'] = calculate_pnl(positions=positions, ticker=ticker, price=price, quantity=quantity)

            positions[ticker]['CurrValue'] = (abs(positions[ticker]['Qty'] * positions[ticker]['LTP'])) # sell - -ve

def place_order(positions, ticker, price, quantity, transaction_type):
    if ticker not in positions:
        update_positions(positions, ticker, price, quantity, transaction_type)

    elif ((positions[ticker]['Qty'] > 0 and transaction_type == 'SELL') or (positions[ticker]['Qty'] < 0 and transaction_type == 'BUY')):
        if quantity > abs(positions[ticker]['Qty']):
            rev_qty = quantity - abs(positions[ticker]['Qty'])
            update_positions(positions,ticker, price, positions[ticker]['Qty'], transaction_type)
            #print("in between")
            #print(positions)
            positions[ticker]['AvgPrice'] = price
            positions[ticker]['LTP'] = price
            update_positions(positions,ticker, price, rev_qty, transaction_type)
        else:
            update_positions(positions,ticker, price, quantity, transaction_type)
    else:
        update_positions(positions,ticker, price, quantity, transaction_type) # position[ticker]['Qty'] = 0
