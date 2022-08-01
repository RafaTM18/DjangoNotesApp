from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('', include('main.urls')),
    path('register', v.register, name='register'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]
