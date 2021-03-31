from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order

def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")


def orders_list(request):
    orders = Order.objects.all()
    context = {"orders" : orders}
    return render(request, "dashboard/order_list.html", context)