from django.conf.urls import patterns, url
from AGEs.views import home_views, person_views, picture_views, post_views

urlpatterns = patterns('',
        url(r'^$', home_views.home, name='home'),
        url(r'^about/$', home_views.about, name='about'),
        url(r'^person/$', person_views.person, name='person'),
        url(r'^add_person/$', post_views.add_person, name='add_person'),
        url(r'^add_picture/(?P<slug>[\w\-]+)$', post_views.add_picture, name='add_picture'),
        # (?P<***>)は変数を渡す時に使う。
        url(r'^item/(?P<item_name_slug>[\w\-]+)/$', picture_views.personname, name='item'),
        )
