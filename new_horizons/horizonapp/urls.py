from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.guide, name="guide"),
    path('home/', views.home, name="home"),
    path('home-<str:company>', views.home, name='home'),
    path('panaroma/', views.panaroma, name='panaroma'),
    path('blog/<str:slug>', views.blog, name='blog'),
    path('news/', views.news_blog_archive, name='news'),
    path('news=<int:cat_id>', views.news_blog_archive_category, name='news'),
    path('get_building_rent_info', views.get_building_rent_details, name="get_building_rent_details"),
    path('get-organizations', views.get_organizations, name='get-organizations'),
    path('register-rent', views.register_rent, name='register-rent'),
    path('clear-leaseholder', views.clear_leaseholder, name='clear-leaseholder'),
    path('register-contact-requet', views.register_contact_request, name='register-contact-request'),
    # path('sub/about-us', views.aboutUs, name='about-us'),
    # path('sub/building-structure', views.building_structure, name='building-structure'),
    # path('sub/user-experience', views.user_experience, name='user-experience'),
    # path('sub/security', views.security, name='security'),
    path('sub/<str:sign>', views.subpage, name='subpage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
