import django
from django.contrib import admin
from django.urls import path, include 
from .views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('login/', django.contrib.auth.views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
