from django.shortcuts import render
from .models import Order

def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    data = Order(order_name=name, order_phone=phone)
    data.save()
    return render(request, './thanks_page.html', {'name': name, 'phone': phone})