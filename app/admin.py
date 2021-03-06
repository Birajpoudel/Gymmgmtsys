from django.contrib import admin
from . import models


# Register your models here.
admin.site.site_header = "Arnold's GYM Admin"

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
admin.site.register(models.Banners, BannerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(models.Service, ServiceAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(models.Page, PageAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('Ques',)
admin.site.register(models.Faq, FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_Name','email','message','send_time')
admin.site.register(models.Enquiry,EnquiryAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(models.Gallery, GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
admin.site.register(models.GalleryImage, GalleryImageAdmin)

class SubPlanAdmin(admin.ModelAdmin):
    list_editable = ('highlights_status','max_member')
    list_display = ('title','price','max_member','highlights_status')
admin.site.register(models.SubPlan, SubPlanAdmin)

class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('title','subplans')

    def subplans(self, obj):
        return " | ".join([sub.title for sub in obj.subplan.all()])
admin.site.register(models.SubPlanFeature, SubPlanFeatureAdmin)

class PlanDiscountAdmin(admin.ModelAdmin):
    list_display = ('total_months','total_discount','subplans')
    def subplans(self, obj):
        return " | ".join([sub.title for sub in obj.subplan.all()])

admin.site.register(models.PlanDiscount,PlanDiscountAdmin)


class subscriberAdmin(admin.ModelAdmin):
    list_display = ('user','image_tag','phone_number','address')
admin.site.register(models.subscriber,subscriberAdmin)

class subscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','plan','price')
admin.site.register(models.subcription,subscriptionAdmin)