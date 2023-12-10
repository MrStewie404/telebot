import config as cfg
import requests
import telebot

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        try: 
            quote = cfg.keys.get(quote)
        except:
            raise CurrencyConverter(cfg.error.get("currency").replace("currency", quote))
            
        try: 
            base = cfg.keys.get(base)
        except:
            raise CurrencyConverter(cfg.error.get("currency").replace("currency", base))
        
        try:
            url = f'https://v6.exchangerate-api.com/v6/{cfg.api_key}/latest/{quote}'
            response = requests.get(url)
            data = response.json()
            answer = data["conversion_rates"][base] * float(amount)
        except:
            raise CurrencyConverter(cfg.error.get("internet"))

        return answer