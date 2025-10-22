import requests
from datetime import datetime

def main(context):
    try:
        # دریافت داده از درخواست
        data = context.req.body
        
        if isinstance(data, str):
            import json
            data = json.loads(data)
        
        # اطلاعات پیام تلگرام
        message = data.get('message', {})
        text = message.get('text', '')
        chat_id = message.get('chat', {}).get('id')
        
        # اگر پیام /start بود
        if text == '/start':
            response_text = "🤖 به ربات تریدینگ خوش آمدید!\n\n"
            response_text += "دستورات:\n"
            response_text += "/price - قیمت بیت‌کوین\n"
            response_text += "/analysis - تحلیل بازار"
        
        # اگر پیام /price بود
        elif text == '/price':
            # دریافت قیمت از Binance
            url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
            response = requests.get(url)
            price_data = response.json()
            current_price = float(price_data['price'])
            
            response_text = f"💰 قیمت بیت‌کوین:\n"
            response_text += f"{current_price:,.0f} دلار\n\n"
            response_text += f"⏰ زمان: {datetime.now().strftime('%H:%M')}"
        
        else:
            response_text = "دستور نامعتبر! از /start استفاده کنید."
        
        # ارسال پاسخ به تلگرام
        telegram_token = context.req.env.get('TELEGRAM_BOT_TOKEN')
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': response_text,
            'parse_mode': 'HTML'
        }
        
        requests.post(url, json=payload)
        
        return context.res.json({'success': True})
        
    except Exception as e:
        return context.res.json({
            'success': False,
            'error': str(e)
        })
