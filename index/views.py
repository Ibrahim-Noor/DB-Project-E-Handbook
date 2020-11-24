from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    context = {}
    return render(request, 'index/index.html', context)