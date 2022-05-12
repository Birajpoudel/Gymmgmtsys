from django.contrib import admin
from . import models


# Register your models here.

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