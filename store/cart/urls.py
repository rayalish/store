from django.urls import path
from .views import *


urlpatterns = [
    path('', CartView.as_view()),
    path('order/', OrderAPI.as_view())
]