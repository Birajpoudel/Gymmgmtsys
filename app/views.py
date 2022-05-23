from django.shortcuts import  render,redirect
from app import models
from app import forms

def BASE(request):
    return render (request, 'base.html')

#Home page
def HOME(request):
    banners = models.Banners.objects.all()
    services = models.Service.objects.all()[:4]

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

#Subscription Plans
def PRICING(request):
    pricing=models.SubPlan.objects.all().order_by('price')
    dfeatures = models.SubPlanFeature.objects.distinct('title')


    return render (request,'pricing.html',{'plans':pricing,'dfeatures':dfeatures})

from app.Emailbackend  import EmailBackEnd
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
def DO_LOGIN(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')

    return render(request,'registration/login.html')
def Error404(request):
    return render(request,'404.html')

#Signup
def signup(request):
    msg = None
    if request.method == 'POST':
        form=forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            msg='Thank you for registration.'

    form=forms.SignUp
    return render(request, 'registration/signup.html',{'form':form,'msg':msg})

#Checkout
def CHECKOUT(request,plan_id):
    planDetail=models.SubPlan.objects.get(pk=plan_id)


    return render (request,'checkout.html',{'plan':planDetail})