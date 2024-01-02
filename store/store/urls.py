from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from . import settings

schema_view = get_swagger_view(title='Store API')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    
    path('authe/users/', include('authe.urls')),
    path('api/product/', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)