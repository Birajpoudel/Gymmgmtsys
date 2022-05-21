from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

