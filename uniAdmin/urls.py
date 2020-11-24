from django.urls import path
from .views import *

urlpatterns = [
    path('', adminLoginView, name="adminLogin"),
    path('admin-mainpage/', adminMainPageView, name="adminMainPage"),
    ]