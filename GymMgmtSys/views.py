from django.shortcuts import  render
from app import models
from app import forms


#Home page
def HOME(request):
    banners = models.Banners.objects.all()
    services = models.Service.objects.all()[:3]

    return render (request, 'home.html',{'banners':banners,'services':services})

#FAQ
def FAQ(request):
    faq=models.Faq.objects.all()
    return render(request,'faq.html',{'faqs':faq})
#Enquiry
def ENQUIRY(request):
    msg=''
    if request.method=="POST":
        form=forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Data has been saved'
    form= forms.EnquiryForm
    return render(request, 'enquiry.html', {'form': form,'msg':msg})


def BASE(request):
    return render (request, 'base.html')
def PRICING(request):
    return render (request, 'pricing.html')

