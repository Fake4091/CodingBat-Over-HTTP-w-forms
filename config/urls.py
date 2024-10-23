"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import front_view, no_teen_view, xyz_view, centered_avg_view

urlpatterns = [
    path("warmup-2/font-times", front_view, name="front_times"),
    path("logic-2/no-teen-sum", no_teen_view, name="no_teen"),
    path("string-2/xyz-there", xyz_view, name="xyz_there"),
    path("list-2/centered-average", centered_avg_view, name="centered_avg"),
]
