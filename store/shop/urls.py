from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('categ/', views.ListCreateCategAPIView.as_view(), name='categ_list_create'),   
    path('categ/one/<int:pk>/', views.RetrieveCategAPIView.as_view(), name='categ_one'),
    path('categ/delete/<int:pk>/', views.DestroyCategAPIView.as_view(), name='categ_delete'),
    path('categ/update/<int:pk>/', views.UpdateCategAPIView.as_view(), name='categ_update'),

    path('', views.ProductAPIView.as_view(), name='shop'),
    path('detail/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),

    path('categ/<int:category_id>/products/', views.ProductByCategoryList.as_view(), name='products-by-category')
]