import requests
from datetime import datetime

def main(context):
    try:
        # دریافت قیمت
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        price_data = response.json()
        current_price = float(price_data['price'])
        
        result = {
            'success': True,
            'price': current_price,
            'symbol': 'BTCUSDT',
            'message': 'قیمت دریافت شد! 🎉'
        }
        
        # چاپ نتیجه در لاگ
        context.log(f"قیمت بیت‌کوین: {current_price}")
        
        return context.res.json(result)
        
    except Exception as e:
        context.log(f"خطا: {str(e)}")
        return context.res.json({
            'success': False,
            'error': str(e)
        })
