from django.conf.urls import url
from login import views
from django.contrib.auth.views import login as auth_login, logout as auth_logout

urlpatterns = [
    url(r'analysis/$', views.twitter, name = 'feature')
]
