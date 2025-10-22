import requests
from datetime import datetime

def main(context):
    try:
        # دریافت قیمت
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        price_data = response.json()
        
        result = {
            'success': True,
            'price': float(price_data['price']),
            'message': 'درست شد! 🎉'
        }
        
        # در AppWrite جدید باید اینطور برگردونیم
        return context.res.json(result)
        
    except Exception as e:
        return context.res.json({
            'success': False,
            'error': str(e)
        })
