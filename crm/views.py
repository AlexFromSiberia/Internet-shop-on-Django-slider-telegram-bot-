from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import send_telegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    price_table = PriceTable.objects.all()
    price_cards = PriceCard.objects.all()
    form = OrderForms()

    context = {'slider_list': slider_list,
               'price_table': price_table,
               'price_cards': price_cards,
               'form': form}
    return render(request, 'index.html', context)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    data = Order(order_name=name, order_phone=phone)
    data.save()
    # Имя и Тел мы передадим в send_telegram во время обработки POST запроса
    send_telegram(tg_name = name, tg_phone = phone)
    return render(request, 'thanks.html', {'name': name})
