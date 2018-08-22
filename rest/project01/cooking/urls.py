from django.urls import path

from . import views
#DAMMMMMMMMMMMMMMMMMMMMMMM

# add email/ on the path to be called as action on forms
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('testFiltrar/', views.testFiltrar, name='testFiltrar'),
    path('filtrar/', views.filtrar, name='filtrar'),    
    path('testEmail/', views.testEmail, name='testEmail'),     
    path('email/', views.email, name='email'),
    path('usuarios/', views.usuario_list, name='usuario_list'),#apirest usuarios
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),#apirest usuarios by id
]

"""
from django.conf.urls import url

from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
"""
