"""GymMgmtSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('base/', views.BASE, name='base'),
    path('pricing/', views.PRICING, name='pricing'),
    path('faq', views.FAQ, name='faq'),
    path('enquiry', views.ENQUIRY, name='enquiry'),
    path('pagedetail/<int:id>', views.page_detail, name='pagedetail'),


    path('gallery', views.gallery, name='gallery'),
    path('gallery_detail/<int:id>', views.gallery_detail, name='gallery_detail'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('login', views.DO_LOGIN, name='login'),
    path('404', views.Error404, name='404'),
    path('accounts/signup',views.signup,name='signup' ),
    path('checkout/<int:plan_id>',views.CHECKOUT,name='checkout'),
    #path('checkout_session/<int:plan_id>',views.checkout_session(),name='checkout_session'),
    path('pay_success',views.pay_success,name='pay_success'),
    path('pay_cancel', views.pay_cancel, name='pay_cancel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

