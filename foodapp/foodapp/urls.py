"""
URL configuration for foodapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, re_path
# from django.conf.urls import include
# from django.http import HttpResponse
#
#
# # Tạo một view đơn giản cho trang chính
# def home(request):
#     return HttpResponse("Welcome to the homepage!")
#
#
# urlpatterns = [
#
#     path('admin/', admin.site.urls),
#     re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
#     path('', home),  # Thêm đường dẫn cho trang chính
# ]
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

from django.http import HttpResponse
from food.admin import admin_site

# Tạo một view đơn giản cho trang chính
def home(request):
    return HttpResponse("Welcome to the homepage!")


urlpatterns = [
    path('', include('food.urls')),
    path('admin/', admin_site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', home),
]
