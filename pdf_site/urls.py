from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

    path('books/', include('books.urls'), name='books'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
