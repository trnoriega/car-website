from django.conf.urls import url

from . import views

app_name = 'grad_school'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about', views.about, name='about'),
    url(r'main-project', views.main_project, name='main_project'),
    url(r'static-dynamic', views.static_dynamic, name='static_dynamic'),
    url(r'dynamic-dynamic', views.dynamic_dynamic, name='dynamic_dynamic'),
    url(r'simulation', views.simulation, name='simulation'),
    url(r'mitos', views.mitos, name='mitos'),
]
