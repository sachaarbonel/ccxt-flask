import ccxt  # noqa: E402
from flask import Flask, jsonify

app = Flask(__name__)
exchanges = {}  # a placeholder for your instances

for id in ccxt.exchanges:
    exchange = getattr(ccxt, id)
    exchanges[id] = exchange()

@app.route('/ticker/<exchange>/<symbol1>/<symbol2>', methods=['GET'])
def get_ohlcv(exchange,symbol1,symbol2):
    return jsonify(exchanges[exchange].fetch_ohlcv(symbol1+"/"+symbol2))
# now exchanges dictionary contains all exchange instances...

if __name__ == '__main__':
    app.run()