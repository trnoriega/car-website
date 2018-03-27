from django.conf.urls import url

from . import views

app_name = 'classifier'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'predictions', views.predictions, name='predictions'),
    url(r'about', views.about, name='about')
]
