import requests
from .models import Telesettings


"""
через url запрос с помощью api Telegram можно отправлять сообщения ботом
url = f'https://api.telegram.org/bot{token}{api_method}?chat_id={id}&text={text}'
text = 'testing message'
chat_id = '-856774933'
token = '5709386163:AAFhyB5bgrCZQ5khKZZvCoVJY5zZhw4unXI'
api_method = '/sendMessage'
"""


def send_telegram(tg_name, tg_phone):
    if Telesettings.objects.get(pk=1):
        # присвоим settings все данные первого обьекта Telesettings
        # вытащим из них нужные аргументы
        settings = Telesettings.objects.get(pk=1)
        text = str(settings.tg_message)
        chat_id = str(settings.tg_chat)
        token = str(settings.tg_token)
        api = 'https://api.telegram.org/bot'
        api_method = '/sendMessage'
        method = api + token + api_method

        # Чтобы в сообшении от бота вывести "Имя" и "Телефон" клиента, нужно
        # нарезать кусками сообщение которое у нас есть в БД
        # и добавить к нему Имя и Телефон (см ниже)
        # Имя и Тел мы передадим из Views во время обработки POST запроса

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            # текст, который нарезаем: Заявка с сайта. Имя {Name} Телефон {Phone}
            a = text.find('{')
            b = text.find('}')
            c = text.rfind('{')
            d = text.rfind('}')

            # составим итоговое сообщение из полученных частей
            part_1 = text[0:a]
            part_2 = text[b + 1:c]
            part_3 = text[d:-1]
            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slise = text
        try:
            req = requests.post(method, data={'chat_id': chat_id, 'text': text_slise})
        except:
            pass
        finally:
            pass
        if req.status_code != 200:
            print('Ошибка отправки!')
        elif req.status_code == 500:
            print('Ошибка 500')
        else:
            print('Сообщение отправлено!')
    else:
        pass
