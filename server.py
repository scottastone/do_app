import requests
import time
import http.server
import socketserver
from http import HTTPStatus
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'The current price of BTC in CAD is: $%s' % (get_btc_price())
        self.wfile.write(msg.encode())

def get_btc_price() -> str:
    url = 'https://api.coingecko.com/api/v3/exchange_rates'
    data = requests.get(url).json()
    price = data['rates']['cad']['value']
    return price

port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
    