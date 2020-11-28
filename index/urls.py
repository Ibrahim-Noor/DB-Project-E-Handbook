from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name="indexPage"),
    path('access-denied/', accessDeniedView, name="accessDenied"),
    path('logout', logoutView, name="logout"),
    ]