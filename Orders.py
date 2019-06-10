class Orders:

    def __init__(self,
                 exchange,
                 validity,
                 kite,
                 disclosed_quantity=None,
                 live=False,
                 tag=None
                 ):
        self.exchange = exchange
        self.validity = validity
        self.live = live
        self.tag = tag
        self.kite = kite
        self.disclosed_quantity = disclosed_quantity

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
                                    order_type=order_type,
                                    validity=self.validity,
                                    tag=self.tag
                                    )
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
        if self.live:
            return kite.place_order(variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=limitprice,
                                    validity=self.validity,
                                    tag=self.tag
                                    )
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
        if self.live:
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
                                    trailing_stoploss=trailing_stoploss,
                                    validity=self.validity,
                                    tag=self.tag
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
                    variety,
                    price,
                    trigger_price
                    ):
        if self.live:
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
                                    trailing_stoploss=trailing_stoploss,
                                    trigger_price=trigger_price,
                                    validity=self.validity,
                                    disclosed_quantity=self.disclosed_quantity,
                                    tag=self.tag
                                    )
        else:
            execute_order()

    def modify_orders(self):
        pass

    def cancel_orders(self):
        pass




