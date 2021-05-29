from django.contrib import admin
from django.urls import path, include

from rango.views import index

urlpatterns = [
    path('', index, name='index'),
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
]
