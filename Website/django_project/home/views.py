from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')

def projects(request):
	return render(request, 'home/projects.html')