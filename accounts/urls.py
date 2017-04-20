from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/$', views.redirect_profile, name='profile'),
    url(r'^user/(?P<username>\w+)/$', views.profile_page, name='profile_page'),
    url(r'^edit/$', views.edit_profile, name='edit'),
]
