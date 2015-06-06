from django.conf.urls import patterns, url
from AGEs import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        )
