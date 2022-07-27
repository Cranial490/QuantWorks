import pandas as pd
columns = ["variety", "exchange", "tradingsymbol", "transaction_type", "quantity", "product", "order_type", "price",
           "validity", "disclosed_quantity", "trigger_price", "squareoff", "stoploss", "trailing_stoploss", "tag"]
order_book = pd.DataFrame(columns=columns)
print(order_book)


class Storage:
    columns = []
    dataframe = pd.DataFrame()

    def execute_order(self,
                      variety,
                      exchange,
                      tradingsymbol,
                      transaction_type,
                      quantity,
                      product,
                      order_type,
                      price=None,
                      validity=None,
                      disclosed_quantity=None,
                      trigger_price=None,
                      squareoff=None,
                      stoploss=None,
                      trailing_stoploss=None,
                      tag=None):
        params = locals()
        index = order_book.shape[0]
        order_book.loc[index] = list(params.values())
        return index



# this function returns index of the order
# either directly write to csv in this function itself.
# Or create a datastructure to store orders and write after the execution completes.
