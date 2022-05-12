from django.shortcuts import  render
from app import models
from app import forms


#Home page
def HOME(request):
    banners = models.Banners.objects.all()
    services = models.Service.objects.all()[:3]

    return render (request, 'home.html',{'banners':banners,'services':services})
def page_detail(request,id):
    page=models.Page.objects.get(id=id)
    return render(request,'page.html',{'page':page})

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
#Show Gallery
def gallery(request):
    gallery = models.Gallery.objects.all().order_by('-id')
    return render (request, 'gallery.html',{'gallerys':gallery})

#Show Gallery
def gallery_detail(request,id):
    gallery = models.Gallery.objects.get(id=id)
    gallery_imgs = models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render (request, 'gallery_imgs.html',{'gallery_imgs':gallery_imgs,'gallery':gallery})

def BASE(request):
    return render (request, 'base.html')
def PRICING(request):
    return render (request, 'pricing.html')

