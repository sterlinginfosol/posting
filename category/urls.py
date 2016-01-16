from django.conf.urls import patterns,include,url
from category import views
urlpatterns=patterns('',
	url(r'^$', 'category.views.category_list'),
	url(r'^(?P<pk>[0-9]+)/$', 'category.views.category_detail'),
)
