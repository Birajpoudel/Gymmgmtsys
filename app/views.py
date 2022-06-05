from django.shortcuts import  render,redirect
from app import models
from app import forms
import stripe

def BASE(request):
    return render (request, 'base.html')

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


stripe.api_key = 'sk_test_51L4F8ESJsiI7mY7S0wqIIk1jTSNHqsryBiioQg7RSBwTpWnoJQXBRTgjQoRunJ32u8ACnt5OFg0GjUI5gxz8NbIo00SEhxCdj8'


def checkout_session(request,plan_id):
	plan=models.SubPlan.objects.get(pk=plan_id)
	session=stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
	      'price_data': {
	        'currency': 'inr',
	        'product_data': {
	          'name': plan.title,
	        },
	        'unit_amount': plan.price*100,
	      },
	      'quantity': 1,
	    }],
	    mode='payment',

	    success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
	    cancel_url='http://127.0.0.1:8000/pay_cancel',
	    client_reference_id=plan_id
	)
	return redirect(request,session.url, {plan:plan})
def pay_success (request):
    return render(request,'success.html')
def pay_cancel(request):
    return render(request,'cancel.html')