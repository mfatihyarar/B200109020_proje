from django.shortcuts import render

from home.models import Setting

# Create your views here.

def index(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting, "page":"home"}
    return render(request, 'index.html', context)

def about(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting,"page":"about"}
    return render(request, 'about.html', context)

def destination(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting,"page":"destination"}
    return render(request, 'destination.html', context)

def contact(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting,"page":"contact"}
    return render(request, 'contact.html', context)

def packages(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting,"page":"packages"}
    return render(request, 'packages.html', context)
