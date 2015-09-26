"""django_contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login_view, name='login_view'),
    url(r'^contacts_list/', views.contacts_list_view, name='contacts_list_view'),
    url(r'^login_error/', views.login_error_view, name='login_error_view'),
    url(r'^register/', views.register_view, name='register_view'),
]
