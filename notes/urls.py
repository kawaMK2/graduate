from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.top, name='top'),
    url(r'^note/(?P<note_title>\w+)/$', views.note, name='note'),
    url(r'^tag/(?P<tag_id>\w+)/$', views.tag, name='tag'),
    url(r'^edit/(?P<note_title>\w+)/$', views.edit, name='edit')
]
