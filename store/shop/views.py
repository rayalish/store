from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import *
from .serializers import *
from .permissions import *




class ListCreateCategAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes  = (IsAdminOrReadOnly, )

class RetrieveUpdateDestroyCategAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes  = (IsAdminOrReadOnly, )
    




class ListCreateQuanAPIView(ListCreateAPIView):
    queryset = QuantityVariant.objects.all()
    serializer_class = QuantitySerializer
    permission_classes  = (IsAdminOrReadOnly, )

class RetrieveUpdateDestroyQuanAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuantityVariant.objects.all()
    serializer_class = QuantitySerializer
    permission_classes  = (IsAdminOrReadOnly, )






class ListCreateProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes  = (IsAdminOrReadOnly, )
    
class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes  = (IsAdminOrReadOnly, )

    


class ProductByCategoryList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
    
class ProductSearchView(generics.ListAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Product.objects.filter(name__icontains=query)






