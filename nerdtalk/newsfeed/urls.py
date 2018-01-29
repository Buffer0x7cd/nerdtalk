from django.conf.urls import url
from newsfeed import views
urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^home/', views.home, name="home"),
]