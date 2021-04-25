from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . models import Order,OrderItem,Refund
from . forms import RefundForm
from django.views.generic import View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.

def thanks(request,order_id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=order_id)
        order_items =OrderItem.objects.filter(order=order)
        template = render_to_string('email_template.html',{'name':request.user.username , 'product':order_items})
    
        email = EmailMessage(
            'subject',
            template,
            settings.EMAIL_HOST_USER,
            [request.user.email],
            )
        email.fail_silently = False
        email.send()

    if order_id:
        customer_order = get_object_or_404(Order,id=order_id)
    return render(request,'thanks.html',{'customer_order':customer_order})


@login_required()
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
        print(email)
        print(order_details)
    return render(request,'order/orders_list.html',{'order_details':order_details})

@login_required()
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=order_id)
        order_items =OrderItem.objects.filter(order=order)
    return render(request,'order/order_detail.html',{'order':order,'order_items':order_items})

class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {'form': form}
        return render(self.request, "request_refund.html", context)
        
    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST) 
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form .cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            
            try:
                order = Order.objects.get(ref_code=ref_code) 
                order.refund_requested = True
                order.save()  
                refund = Refund()
                refund.order = order
                refund.reason = message 
                refund.email = email
                refund.save()
                messages.info(self.request, "Your refund request has been received.")
                return render(self.request,'refund_complete.html')
            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect('order:request-refund')