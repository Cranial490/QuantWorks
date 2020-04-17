import logging
import util

logging.basicConfig(level=logging.DEBUG)

configPath = '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/config.properties'

kws = util.get_ticker_instance(configPath)


def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Starting the data stream")
    logging.debug("Ticks: {}".format(ticks))


def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    logging.debug("Starting the connection")
    # Set RELIANCE to tick in `full` mode.
    ws.subscribe([14451970])
    ws.set_mode(ws.MODE_QUOTE, [14451970])
    logging.debug("successfully subscribed: ")


def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    print("Closing the connection")
    ws.stop()



# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
