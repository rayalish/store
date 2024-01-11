from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.



class CartView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self , request):
        user = request.user
        cart = Cart.objects.filter(user = user, ordered=False).first()
        queryset = CartItems.objects.filter(cart = cart)
        serializer = CartItemsSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user = user, ordered = False)

        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItems(cart = cart, user = user, product = product, price = price, quantity = quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItems.objects.filter(user = user, cart = cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()

        return Response({'success': 'Items added to your cart'})    
    
    def put(self , request):
        data = request.data
        cart_item = CartItems.objects.get(id = data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success':'Items upload'})
    
    def delete(self , request):
        user = request.user
        data = request.data

        cart_item = CartItems.objects.get(id = data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user = user, ordered = False).first()
        queryset = CartItems.objects.filter(cart = cart)
        serializer = CartItemsSerializer(queryset, many = True)
        return Response(serializer.data)
    




    

# views.py
class CartToOrderView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        queryset = Orders.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Получение данных из корзины пользователя
        cart_items = CartItems.objects.filter(user=request.user)

        # Проверка, что корзина не пуста
        if not cart_items.exists():
            return Response({'detail': 'Корзина пуста'}, status=status.HTTP_400_BAD_REQUEST)

        # Создание заказа
        total_amount = sum(item.price for item in cart_items)

        order_serializer = self.get_serializer(data={'user': request.user.id, 'cart': cart_items[0].cart.id, 'amount': total_amount, 'is_paid': True})
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()

        # Очистка корзины
        cart_items.delete()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)