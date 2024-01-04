from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('categ/', views.ListCreateCategAPIView.as_view(), name='categ-list'),
    path('categ/one/<int:pk>/', views.RetrieveUpdateDestroyCategAPIView.as_view(), name='categ_one'), 
    path('categ/<int:category_id>/products/', views.ProductByCategoryList.as_view(), name='products-by-category'),  
    path('', views.ListCreateCategAPIView.as_view(), name='shop'),
    path('search/', views.ProductSearchView.as_view(), name = 'products-search'),

    path('quantity_type/', views.ListCreateQuanAPIView.as_view(), name='quantity-type-list'), 
    path('quantity_type/one/<int:pk>/', views.RetrieveUpdateDestroyCategAPIView.as_view(), name='quantity-type-one'),
    
    path('detail/<int:pk>/', views.RetrieveUpdateDestroyProductAPIView.as_view(), name='product-detail'),

    
    path('admin/create/', views.ListCreateProductAPIView.as_view(), name= 'admin-product'),
    path('admin/delete/<int:pk>/', views.RetrieveUpdateDestroyProductAPIView.as_view(), name= 'admin-product'),
    path('admin/update/<int:pk>/', views.RetrieveUpdateDestroyProductAPIView.as_view(), name= 'admin-product'),

    path('admin/categ/', views.ListCreateCategAPIView.as_view(), name='admin-categ-create'),
    path('admin/categ/delete/<int:pk>/', views.RetrieveUpdateDestroyCategAPIView.as_view(), name='admin-categ-delete'),
    path('admin/categ/update/<int:pk>/', views.RetrieveUpdateDestroyCategAPIView.as_view(), name='admin-categ-update'),

    path('admin/quantity_type/create/', views.ListCreateQuanAPIView.as_view(), name='admin-quantity-type-create'),
    path('admin/quantity_type/delete/<int:pk>/', views.RetrieveUpdateDestroyQuanAPIView.as_view(), name='admin-quantity-type-delete'),
    path('admin/quantity_type/update/<int:pk>/', views.RetrieveUpdateDestroyQuanAPIView.as_view(), name='admin-quantity-type-update'),
]