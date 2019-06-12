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
            return kite.place_order(self,
                                    variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=None,
                                    validity=self.validity,
                                    disclosed_quantity=self.disclosed_quantity,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag=self.tag
                                    )
        else:
            execute_order(self,
                          variety=variety,
                          exchange=self.exchange,
                          tradingsymbol=symbol,
                          transaction_type=transaction_type,
                          quantity=quantity,
                          product=product,
                          order_type=order_type,
                          price=None,
                          validity=self.validity,
                          disclosed_quantity=self.disclosed_quantity,
                          trigger_price=None,
                          squareoff=None,
                          stoploss=None,
                          trailing_stoploss=None,
                          tag=self.tag)

    def limit_order(self,
                    symbol,
                    order_type,
                    transaction_type,
                    product,
                    quantity,
                    variety,
                    limitprice):
        if self.live:
            return kite.place_order(self,
                                    variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=limitprice,
                                    validity=self.validity,
                                    disclosed_quantity=self.disclosed_quantity,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag=self.tag
                                    )
        else:
            execute_order(self,
                          variety=variety,
                          exchange=self.exchange,
                          tradingsymbol=symbol,
                          transaction_type=transaction_type,
                          quantity=quantity,
                          product=product,
                          order_type=order_type,
                          price=limitprice,
                          validity=self.validity,
                          disclosed_quantity=self.disclosed_quantity,
                          trigger_price=None,
                          squareoff=None,
                          stoploss=None,
                          trailing_stoploss=None,
                          tag=self.tag)

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
                      price):
        if self.live:
            return kite.place_order(self,
                                    variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=price,
                                    validity=self.validity,
                                    disclosed_quantity=self.disclosed_quantity,
                                    trigger_price=None,
                                    squareoff=target,
                                    stoploss=stop_loss,
                                    trailing_stoploss=trailing_stoploss,
                                    tag=self.tag
                                    )
        else:
            execute_order(self,
                          variety=variety,
                          exchange=self.exchange,
                          tradingsymbol=symbol,
                          transaction_type=transaction_type,
                          quantity=quantity,
                          product=product,
                          order_type=order_type,
                          price=price,
                          validity=self.validity,
                          disclosed_quantity=self.disclosed_quantity,
                          trigger_price=None,
                          squareoff=target,
                          stoploss=stop_loss,
                          trailing_stoploss=trailing_stoploss,
                          tag=self.tag)

    def cover_order(self,
                    symbol,
                    order_type,
                    transaction_type,
                    product,
                    quantity,
                    stop_loss,
                    variety,
                    price,
                    trigger_price
                    ):
        if self.live:
            return kite.place_order(self,
                                    variety=variety,
                                    exchange=self.exchange,
                                    tradingsymbol=symbol,
                                    transaction_type=transaction_type,
                                    quantity=quantity,
                                    product=product,
                                    order_type=order_type,
                                    price=price,
                                    validity=self.validity,
                                    disclosed_quantity=self.disclosed_quantity,
                                    trigger_price=trigger_price,
                                    squareoff=None,
                                    stoploss=stop_loss,
                                    trailing_stoploss=None,
                                    tag=self.tag
                                    )
        else:
            execute_order(self,
                          variety=variety,
                          exchange=self.exchange,
                          tradingsymbol=symbol,
                          transaction_type=transaction_type,
                          quantity=quantity,
                          product=product,
                          order_type=order_type,
                          price=price,
                          validity=self.validity,
                          disclosed_quantity=self.disclosed_quantity,
                          trigger_price=trigger_price,
                          squareoff=None,
                          stoploss=stop_loss,
                          trailing_stoploss=None,
                          tag=self.tag)

    def modify_orders(self):
        pass

    def cancel_orders(self):
        pass




