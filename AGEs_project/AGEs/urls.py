from django.conf.urls import patterns, url
from AGEs import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^person/$', views.person, name='person'),
        url(r'^item/(?P<item_name_slug>[\w\-]+)/$', views.personname, name='item'),
        )
