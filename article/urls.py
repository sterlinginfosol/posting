
from django.conf.urls import patterns,include,url
from article import views
urlpatterns=patterns('',
	url(r'^$', 'article.views.article_list'),
	url(r'^(?P<pk>[0-9]+)/$', 'article.views.article_detail'),
)




