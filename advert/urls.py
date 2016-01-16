from django.conf.urls import patterns,include,url
from advert import views
urlpatterns=patterns('',
	url(r'^$', 'advert.views.advert_list'),
	url(r'^(?P<pk>[0-9]+)/$', 'advert.views.advert_detail'),
)




