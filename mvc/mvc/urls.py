"""mvc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from estados.cookies import cookies_demo
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_example import views,urls
from norelational import views,urls
from estados.sessions import session_demo,session_demo2
#router = routers.DefaultRouter()
#router.register(r'usuario', views.UsuarioViewSet)
#router.register(r'servicio', views.ServicioViewSet)
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url('index/',include(urls)),
    url('editing/',include(urls)),
    url(r'^norelational/', views.index, name='index'),
    url(r'^cookies/?$', cookies_demo, name='demos-cookies'),
    url(r'^sessions/?$', session_demo, name='demos-sessions'),
    url(r'^sessions/2/?$', session_demo2, name='demos-sessions2'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


