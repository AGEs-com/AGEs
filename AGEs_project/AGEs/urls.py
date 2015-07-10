from django.conf.urls import patterns, url
from AGEs.views import home_views, person_views, picture_views, post_views, search_views

urlpatterns = patterns('',
        url(r'^$', home_views.home, name='home'),
        url(r'^about/$', home_views.about, name='about'),
        # Person関連のURL
        url(r'^search/$', search_views.search_person, name='search'),
        url(r'^search_picture/(?P<id>[\w\-]+)$', search_views.search_picture, name='search_picture'),
        url(r'^person/$', person_views.person, name='person'),
        url(r'^add_person/$', post_views.add_person, name='add_person'),
        url(r'^add_picture/(?P<id>[\w\-]+)$', post_views.add_picture, name='add_picture'),
        # (?P<***>)は変数を渡す時に使う。
        url(r'^item/(?P<id>[\w\-]+)/$', picture_views.personname, name='item'),

        # Object関連のURL
        url(r'^object/$', person_views.object, name='object'),
        )
