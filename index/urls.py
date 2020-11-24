from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name="indexPage"),
    ]