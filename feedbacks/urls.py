from django.conf.urls import patterns , url
from feedbacks import views
urlpatterns = patterns('',url(r'^$', views.index, name='index'),
													
													
)
