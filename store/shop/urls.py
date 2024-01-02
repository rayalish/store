from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('categ/', views.ListCreateCategAPIView.as_view(), name='categ_list_create'),   
    path('categ/one/<int:pk>/', views.RetrieveCategAPIView.as_view(), name='categ_one'),
    path('categ/delete/<int:pk>/', views.DestroyCategAPIView.as_view(), name='categ_delete'),
    path('categ/update/<int:pk>/', views.UpdateCategAPIView.as_view(), name='categ_update'),

    path('quantity_type/', views.ListCreateQuanAPIView.as_view(), name='quantity_type_list_create'),   
    path('quantity_type/one/<int:pk>/', views.RetrieveQuanAPIView.as_view(), name='quantity_type_one'),
    path('quantity_type/delete/<int:pk>/', views.DestroyQuanAPIView.as_view(), name='quantity_type_delete'),
    path('quantity_type/update/<int:pk>/', views.UpdateQuanAPIView.as_view(), name='quantity_type_update'),

    path('', views.ProductAPIView.as_view(), name='shop'),
    path('detail/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),

    path('categ/<int:category_id>/products/', views.ProductByCategoryList.as_view(), name='products-by-category'),

    path('search/', views.ProductSearchView.as_view(), name = 'products-search')
]