from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ListGroupView.as_view(), name='list-group'),
    url(r'^board/(?P<pk>\d+)/$', views.DetailBoardView.as_view(), name='detail-board'),
    url(r'^topic/(?P<pk>\d+)/$', views.DetailTopicView.as_view(), name='detail-topic'),
]