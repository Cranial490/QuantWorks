import pandas as pd


def create_order_book():
  columns = ["tradingsymbol", "quantity",
             "order_type", "price", "transaction_type"]
  return pd.DataFrame(columns=columns)


def place_order(order_book, ticker, price, quantity, order_type, transaction_type):
  order = pd.DataFrame(
      [[ticker, quantity, order_type, price, transaction_type]], columns=order_book.columns)
  return order_book.append(order)


order_book = create_order_book()
order_book = place_order(order_book, 'ADANI', 15, 10, 'MARKET', 'SELL')
