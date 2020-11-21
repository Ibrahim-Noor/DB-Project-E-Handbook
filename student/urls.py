from django.urls import path
from .views import *

urlpatterns = [
    path('', loginView, name="login"),
    path('e-handbook/', mainPageView, name="mainPage"),
    path('courses-taken/', coursesTakenView, name='coursesTaken'),
    path('courses-required/', coursesRequiredView, name='coursesRequired'),
    path('check-prereqs/', checkPreReqView, name="checkPreReq"),
]