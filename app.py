import dash
import dash_core_components as dcc
import dash_html_components as html
# from ohlcv_exchanges import load_ohlcv_exchanges
from dynamically import Exchange
from time import sleep

app = dash.Dash()

#names = load_ohlcv_exchanges()
names = ['_1btcxe', 'acx', 'allcoin', 'anxpro', 'binance', 'bit2c', 'bitbay', 'bitcoincoid', 'bitfinex', 'bitfinex2', 'bitflyer', 'bithumb', 'bitlish', 'bitmarket', 'bitmex', 'bitso', 'bitstamp', 'bitstamp1', 'bittrex', 'bl3p', 'bleutrade', 'btcbox', 'btcchina', 'btcexchange', 'btcmarkets', 'btctradeua', 'btcturk', 'btcx', 'bxinth', 'ccex', 'cex', 'chbtc', 'chilebit', 'coincheck', 'coinexchange', 'coinfloor', 'coingi', 'coinmarketcap', 'coinmate','coinsecure', 'coinspot', 'dsx', 'exmo', 'foxbit', 'fybse', 'fybsg', 'gatecoin', 'gateio', 'gdax', 'gemini', 'getbtc', 'hitbtc', 'hitbtc2', 'huobi', 'huobicny', 'huobipro', 'independentreserve', 'itbit', 'jubi', 'kraken','kucoin', 'kuna', 'lakebtc', 'liqui', 'livecoin', 'luno', 'lykke', 'mercado', 'mixcoins', 'nova', 'okcoincny','okcoinusd', 'okex', 'paymium', 'poloniex', 'qryptos', 'quadrigacx', 'quoinex', 'southxchange', 'surbitcoin', 'therock', 'tidex', 'urdubit', 'vaultoro', 'vbtc', 'virwox', 'wex', 'zaif', 'zb']
nestedOptions = names[0]

app.layout = html.Div(
    [
        html.Div([
        dcc.Dropdown(
            id='name-dropdown',
            options=[{'label':name, 'value':name} for name in names],
            value = nestedOptions
            ),
            ],style={'width': '20%', 'display': 'inline-block'}),
        html.Div([
        dcc.Dropdown(
            id='opt-dropdown',
            ),
            ],style={'width': '20%', 'display': 'inline-block'}
        ),
        html.Hr(),
        html.Div(id='display-selected-values')
    ]
)

# @app.callback(
#     dash.dependencies.Output('opt-dropdown', 'options'),
#     [dash.dependencies.Input('name-dropdown', 'value')]
# )
# def update_date_dropdown(selected_exchange):
#     ins = Exchange(selected_exchange)
#     #sleep(3)
#     s = list(ins.symbols)
#     return [{'label': i, 'value': i} for i in s]

# @app.callback(
#     dash.dependencies.Output('display-selected-values', 'children'),
#     [dash.dependencies.Input('opt-dropdown', 'value')])
# def set_display_children(selected_value):
#     return 'you have selected {} option'.format(selected_value)


############################################################################
#                           Better implementation                          #
############################################################################
@app.callback(
    dash.dependencies.Output('opt-dropdown', 'options'),
    [dash.dependencies.Input('name-dropdown', 'value')])
def set_pairs_options(selected_exchange):
    ins = Exchange(selected_exchange)
    s = list(ins.symbols)
    return [{'label': i, 'value': i} for i in s]

@app.callback(
    dash.dependencies.Output('opt-dropdown', 'value'),
    [dash.dependencies.Input('opt-dropdown', 'options')])
def set_pairs_value(available_options):
    return available_options[0]['value']

@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('name-dropdown', 'value'),
     dash.dependencies.Input('opt-dropdown', 'value')])
def set_display_children(selected_exchange, selected_pairs):
    return u'you have selected exchange {} and pairs {}'.format(
        selected_exchange, selected_pairs,
    )


if __name__ == '__main__':
    app.run_server()