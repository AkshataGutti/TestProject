from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.details, name='detail'),
    url(r'^user', views.User, name='user'),
    url(r'^home', views.home, name='home'),
    url(r'^search/$', views.Search, name='search')
]
