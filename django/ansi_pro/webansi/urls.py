from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addhosts/$', views.addhosts, name='addhosts'),
    url(r'^addmodules/$', views.addmodules, name='addmodules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
]


