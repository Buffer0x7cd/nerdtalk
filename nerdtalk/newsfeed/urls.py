from django.conf.urls import url
from newsfeed import views
urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^home/', views.post_list, name="home"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/knew/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.delete, name='post_remove'),
]