class Orders:

    def __init__(self,
                 exchange,
                 validity,
                 kite,
                 live=False,
                 tag=None
                 ):
        self.exchange = exchange
        self.validity = validity
        self.live = live
        self.tag = tag
        self.kite = kite

    def market_order(self,
                     symbol,
                     order_type,
                     transaction_type,
                     product,
                     quantity,
                     variety):
        if self.live:
            return kite.place_order(variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type)
        else:
            execute_order()



    def limit_order(self,
                   symbol,
                   order_type,
                   transaction_type,
                   product,
                   quantity,
                   variety,
                   limitprice):
        if(self.live):
            return kite.place_order(variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=limitprice)
        else:
            execute_order()

    def bracket_order(self,
                      symbol,
                      order_type,
                      transaction_type,
                      product,
                      quantity,
                      stop_loss,
                      target,
                      trailing_stoploss,
                      variety,
                      price
                     ):
        if(self.live):
            return kite.place_order(variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=price,
                                    stoploss=stop_loss,
                                    squareoff=target,
                                    trailing_stoploss=trailing_stoploss
                                    )
        else:
            execute_order()

    def cover_order(self,
                    symbol,
                    order_type,
                    transaction_type,
                    product,
                    quantity,
                    stop_loss,
                    target,
                    trailing_stoploss,
                    validity,
                    variety,
                    price,
                    trigger_price
                    ):
        pass

    def modify_orders(self):
        pass

    def cancel_orders(self):
        pass




