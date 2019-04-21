from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('Create', views.createSet, name='createSet'),
	path('Create/', views.createSet, name='createSet'),
	path('ViewAll', views.viewAll, name='viewAll'),
	path('Random', views.random, name='random'),
	path('ViewCards', views.viewCard, name='viewCard'),
	path('SetCreated', views.setCreated, name='setCreated'),
	path('viewSet', views.viewSet, name='viewSet'),
]