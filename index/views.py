from django.shortcuts import render
from .decorators import *
# Create your views here.
@isNotLoggedIn
def indexPageView(request):
    context = {}
    print(request.session.keys())
    return render(request, 'index/index.html', context)

def accessDeniedView(request):
    context = {}
    return render(request, 'index/accessDenied.html', context)

def logoutView(request):
    context = {}
    print("entered")
    request.session.flush()
    print(request.session.keys())
    return redirect("indexPage")