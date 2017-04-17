from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/$', views.redirect_profile, name='profile'),
    url(r'^(?P<username>\w+)/$', views.profile_page, name='profile_page'),
]
