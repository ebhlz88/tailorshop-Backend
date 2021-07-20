"""tailorshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tailor import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customersearch', views.customersearch.as_view()),
    path('ordersearch', views.ordersearch.as_view()),
    path('customerpost', views.customerclass.as_view()),
    path('orderget/<int:pk>', views.orderclass.as_view()),
    path('orderpost', views.orderpost.as_view()),
    path('orderupdate/<int:pkk>', views.orderupdate.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
