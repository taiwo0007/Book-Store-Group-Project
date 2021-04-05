from django.test import TestCase
from . models import Order, OrderItem
from django.urls import reverse, resolve, reverse_lazy
from datetime import datetime

class TestModels(TestCase):

    def setUp(self):
        self.Order1 = Order.objects.create(
            token = 'eqwgvbwkigbv',
            ref_code = 'cqvqvfqf12',
            total = 20.00,
            emailAddress = 'email@email.com',
            created = datetime(2020, 5, 17),
            billingName = 'ShipName',
            billingAddress1 = 'Address1',
            billingCity = 'Rome',
            billingPostcode = 'SPY266',
            billingCountry = 'Italy',
            shippingName = 'ShipName',
            shippingAddress1 = 'Address1',
            shippingCity = 'Rome',
            shippingPostcode = 'SPY266',
            shippingCountry = 'Italy',
            being_delivered = False,
            refund_requested = False,
            refund_granted = False,
        )
        self.OrderItem1 = OrderItem.objects.create(
            product = 'book',
            quantity = 2,
            price = 10.00,
            order = self.Order1,
        )

    def test_order_create_success(self):
        self.assertEqual(f'{self.Order1.token}', 'eqwgvbwkigbv')
        self.assertEqual(f'{self.Order1.ref_code}', 'cqvqvfqf12')
        self.assertEqual(self.Order1.total, 20.00)
        self.assertEqual(f'{self.Order1.emailAddress}', 'email@email.com')
        self.assertEqual(f'{self.Order1.billingName}', 'ShipName')
        self.assertEqual(f'{self.Order1.billingAddress1}', 'Address1')
        self.assertEqual(f'{self.Order1.billingCity}', 'Rome')
        self.assertEqual(f'{self.Order1.billingPostcode}', 'SPY266')
        self.assertEqual(f'{self.Order1.billingCountry}', 'Italy')
        self.assertEqual(f'{self.Order1.shippingName}', 'ShipName')
        self.assertEqual(f'{self.Order1.shippingAddress1}', 'Address1')
        self.assertEqual(f'{self.Order1.shippingCity}', 'Rome')
        self.assertEqual(f'{self.Order1.shippingPostcode}', 'SPY266')
        self.assertEqual(f'{self.Order1.shippingCountry}', 'Italy')
        self.assertFalse(self.Order1.being_delivered)
        self.assertFalse(self.Order1.refund_requested)
        self.assertFalse(self.Order1.refund_granted)

    def test_order_item_create_success(self):
        self.assertEqual(f'{self.OrderItem1.product}', 'book')
        self.assertEqual(self.OrderItem1.quantity, 2)
        self.assertEqual(self.OrderItem1.price, 10.00)
        self.assertEqual(self.OrderItem1.order, self.Order1)

class TestViews(TestCase):

    def test_thanks(self):
        response = self.client.get(reverse('order:thanks',args=['1']))
        self.assertEqual(response.status_code,404)
    
    def test_thanks(self):
        response = self.client.get(reverse('order:thanks',args=['1']))
        self.assertEqual(response.status_code,404)