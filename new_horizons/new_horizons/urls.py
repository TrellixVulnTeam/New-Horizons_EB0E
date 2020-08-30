"""new_horizons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    re_path(r'^jet/', include('jet.urls', 'jet')),
    # re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    path('admin/', admin.site.urls),
    path('', include('horizonapp.urls')),
    path('secret/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('grappelli/', include('grappelli.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)