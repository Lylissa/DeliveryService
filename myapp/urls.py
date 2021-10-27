"""myapp URL Configuration

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
from django.urls import include,path
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from ClickToEat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.loginpage_view, name="loginpage"),
    path('registration', views.registrationpage_view, name="registrationpage"),
    path('home', views.homepage_view, name="homepage"),
    path('partner', views.partnerpage_view, name="partnerpage"),
    path('terms', views.termpage_view, name="termspage"),
    path('privacy', views.privacypage_view, name="privacypage"),
    path('about', views.aboutpage_view, name="aboutpage"),
    path('features', views.featurespage_view, name="featurespage"),
    path('contact', views.contactpage_view, name="contactpage"),
    path('report', views.dashboardpage_view, name="dashboardpage"),
    path('client', views.InsertClient, name="client"),
    path('orders', views.InsertOrders, name="orders"),
    path('rider', views.InsertRider, name="rider"),
    path('store', views.InsertStore, name="store"), 
]
