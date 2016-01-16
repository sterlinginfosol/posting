from django.conf.urls import patterns,include,url
from rest_framework.urlpatterns import format_suffix_patterns
from userprofile import views
urlpatterns=patterns('',
	url(r'^$', 'userprofile.views.user_list'),
	url(r'^(?P<pk>[0-9]+)/$', 'userprofile.views.user_detail'),
)
