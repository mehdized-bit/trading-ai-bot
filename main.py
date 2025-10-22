import requests
from datetime import datetime

def main(context):
    try:
        # دریافت قیمت بیت‌کوین
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        price_data = response.json()
        
        result = {
            'success': True,
            'symbol': 'BTCUSDT', 
            'price': float(price_data['price']),
            'action': 'HOLD', 
            'timestamp': datetime.now().isoformat(),
            'message': 'کار میکنه! 🎉'
        }
        
        return context.response.json(result)
        
    except Exception as e:
        return context.response.json({
            'success': False,
            'error': str(e)
        })
