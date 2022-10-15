from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable


def first_page(request):
    slider_list = CmsSlider.objects.all()
    price_table = PriceTable.objects.all()
    form = OrderForms()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pc_4 = PriceCard.objects.get(pk=4)
    dict1 = {'slider_list': slider_list,
             'price_table': price_table,
             'pc_1': pc_1,
             'pc_2': pc_2,
             'pc_3': pc_3,
             'pc_4': pc_4,
             'form': form}
    return render(request, 'index.html', dict1)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    data = Order(order_name=name, order_phone=phone)
    data.save()
    return render(request, 'thanks.html', {'name': name})
