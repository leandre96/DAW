from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'), 
		path('delete/<int:u_id>', views.delete, name='delete'),
		path('add/',views.add, name='add'),
		path('update/<int:u_id>',views.update, name='update'),
]
