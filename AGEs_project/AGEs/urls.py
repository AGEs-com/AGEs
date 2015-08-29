from django.conf.urls import patterns, url
from AGEs.views import home_views, item_views, picture_views, post_views, search_views

urlpatterns = patterns('',
        url(r'^$', home_views.home, name='home'),
        url(r'^about/$', home_views.about, name='about'),

        # Person関連のURL
        url(r'^person/$', item_views.show_person, name='person'),
        url(r'^add_person/$', post_views.add_person, name='add_person'),
        # (?P<***>)は変数を渡す時に使う。
        url(r'^person_pictures/(?P<id>[\w\-]+)/$', picture_views.get_person_pictures, name='item'),
        url(r'^add_person_picture/(?P<id>[\w\-]+)$', post_views.add_person_picture, name='add_picture'),
        url(r'^search_person/$', search_views.search_person, name='search'),
        url(r'^search_person_pictures/(?P<id>[\w\-]+)$', search_views.search_person_picture, name='search_picture'),

        # Object関連のURL
        url(r'^object/$', item_views.show_object, name='object'),
        url(r'^add_object/$', post_views.add_object, name='add_object'),
        url(r'^object_pictures/(?P<id>[\w\-]+)/$', picture_views.get_object_pictures, name='item'),
        url(r'^add_object_picture/(?P<id>[\w\-]+)$', post_views.add_object_picture, name='add_object'),
        url(r'^search_object/$', search_views.search_object, name='search'),
        url(r'^search_object_pictures/(?P<id>[\w\-]+)$', search_views.search_object_picture, name='search_picture'),
        )
