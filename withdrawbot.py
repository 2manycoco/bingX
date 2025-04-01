import time
import hmac
import hashlib
import requests

apiKey = 'BINGX_API_KEY'
secret = 'BINGX_SECRET'

coin = 'USDT'
amount = '10'
network = 'TRC20'
address = 'YOUR_WHITELISTED_ADDRESS'
timestamp = str(int(time.time() * 1000))
recvWindow = 5000

params = {
    "coin": coin,
    "address": address,
    "network": network,
    "amount": amount,
    "timestamp": timestamp,
    "recvWindow": recvWindow
}

query_string = "&".join([f"{k}={v}" for k, v in params.items()])
signature = hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

headers = {
    "X-BX-APIKEY": apiKey
}

url = f"https://open-api.bingx.com/openApi/wallet/withdraw/submit?{query_string}&signature={signature}"
response = requests.post(url, headers=headers)
print("BingX withdrawal:", response.json())
