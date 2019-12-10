"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .view import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('01/', api_01),
    path('02/', api_02),
    path('02/<multi_path>/', api_02),  # <int:no_space_with_name>, <just_name_is_ok>  多路径只能靠这种方式了嘛
    path('03/', api_03),
    path('04/', api_04),
    path('05/', api_05),
    path('06/', api_06),
    path('07/', api_07),
    path('08/', api_08),
    path('09/', api_09),
    path('10/', api_10),
    path('11/', api_11),
    path('12/', api_12),
]
