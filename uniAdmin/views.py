from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
def adminLoginView(request):
    context = {}
    form = adminLoginForm()
    if request.method == "POST":
        form = adminLoginForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if roll_number == 'admin' and password == 'admin':
                request.session['admin'] = 'admin'
                return redirect('adminMainPage')
        context['error'] = "Invalid Credentials"
    context['form'] = adminLoginForm()
    return render(request, 'admin/adminLogin.html', context)

def adminMainPageView(request):
    context = {}
    return render(request, 'admin/adminMainPage.html', context)