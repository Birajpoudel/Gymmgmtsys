from django.shortcuts import  render
from app import models


#Home page
def HOME(request):
    banners = models.Banners.objects.all()
    services = models.Service.objects.all()[:3]

    return render (request, 'home.html',{'banners':banners,'services':services})

def BASE(request):
    return render (request, 'base.html')

