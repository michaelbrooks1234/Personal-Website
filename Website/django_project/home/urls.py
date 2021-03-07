from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Website-home'),
	path('about/', views.about, name='Website-home-about'),
	path('projects/', views.projects, name='website-home-projects'),
]