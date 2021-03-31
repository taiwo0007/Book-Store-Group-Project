from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order
from django.db.models import Sum, DecimalField
from django.db.models.functions import Cast

def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")
    
def orders_list(request):
    orders = Order.objects.all()
    context = {"orders" : orders}
    return render(request, "dashboard/order_list.html", context)

def reportsView(request):
    return render(request, 'dashboard/reports.html')

def sales_report(request):
    total_sales = Order.objects.aggregate(my_sum=Cast(Sum('total'), DecimalField(max_digits=30, decimal_places=2)))
    context = {'total_sales':total_sales}
    return render(request, 'dashboard/sales.html', context)