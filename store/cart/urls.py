from django.urls import path
from .views import *


urlpatterns = [
    path('', CartView.as_view())
]