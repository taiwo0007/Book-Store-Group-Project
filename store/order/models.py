from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from vouchers.models import Voucher

# Create your models here.


class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    ref_code = models.CharField(max_length=20)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Euro Order Total')
    emailAddress = models.EmailField(
        max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=10, blank=True)
    billingCountry = models.CharField(max_length=200, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True) 
    shippingPostcode = models.CharField(max_length=10, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)
    being_delivered = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    voucher = models.ForeignKey(
        Voucher, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Euro Price') 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"
