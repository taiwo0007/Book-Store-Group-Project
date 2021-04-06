from django.contrib import admin
from .models import Order,OrderItem,Refund

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)
make_refund_accepted.short_description = 'Update orders to refund granted'

def make_order_shipped(modeladmin, request, queryset):
    queryset.update(being_delivered=True)
make_order_shipped.short_description = 'Update orders to shipped'

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldset = [
    ('Product',{'fields':['product'],}),
    ('Quantity',{'fields':['quantity'],}),
    ('Price',{'fields':['price'],}),
    ]
    readonly_fields = ['product','quantity','price']
    can_delete= False
    max_num = 0	
    template = 'admin/order/tabular.html'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','billingName','emailAddress', 'being_delivered', 'refund_requested', 'refund_granted', 'total']
    list_filter = ['being_delivered', 'refund_requested', 'refund_granted']
    list_display_links = ('id','billingName', 'total')
    search_fields = ['id','billingName','emailAddress', 'ref_code']
    readonly_fields= ['token','total','emailAddress','created','billingName',
                'billingAddress1','billingCity','billingPostcode','billingCountry',
                'shippingName','shippingAddress1','shippingCity','shippingPostcode',
                'shippingCountry']
    fieldset = [
    ('ORDER INFORMATION',{'fields': ['id','token','total','created']}),
    ('BILLING INFORMATION', {'fields':['billingName','billingAddress1','billingCity',
                                     'billingPostcode','billingCountry','emailAddress']}),
    ('SHIPPING INFORMATION',{'fields': ['shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
    ]
    inlines = [
        OrderItemAdmin,
    ]
    actions = [make_refund_accepted, make_order_shipped]
    

    def has_delete_permission(self,request,obj=None):
        return False
    def has_add_permission(self,request):
        return False

admin.site.register(Order,OrderAdmin)
