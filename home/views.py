from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from content.models import Content, Category
from home.models import Setting, ContactFormu, ContactFormMessage

# Create your views here.

def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata = Content.objects.all()[:2]
    packagedata = Content.objects.all()[:3]
    destinationdata=Content.objects.all()[:3]
    category=Category.objects.all()
    context = {'setting': setting,
               "category":category,
               "page":"home",
               "sliderdata":sliderdata,
               "destinationdata":destinationdata,
               "packagedata":packagedata}
    return render(request, 'index.html', context)

def about(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting,"page":"about"}
    return render(request, 'about.html', context)

def destination(request):
    setting=Setting.objects.get(pk=1)
    destinationdata=Content.objects.all()[:20]
    context = {'setting': setting,
               "page":"destination",
               "destinationdata":destinationdata}
    return render(request, 'destination.html', context)

def packages(request):
    setting=Setting.objects.get(pk=1)
    packagedata = Content.objects.all()[:20]
    context = {'setting': setting,
               "page":"packages",
               "packagedata":packagedata}
    return render(request, 'packages.html', context)

def contact(request):

    if request.method=="POST":
        form= ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name = form.cleaned_data["name"]
            data.email = form.cleaned_data["email"]
            data.subject = form.cleaned_data["subject"]
            data.message = form.cleaned_data["message"]
            data.ip=request.META.get("REMOTE_ADDR")
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir")
            return HttpResponseRedirect("/contact")

    setting=Setting.objects.get(pk=1)
    form=ContactFormu()
    context={"setting":setting,"form":form}
    return render(request,"contact.html",context)