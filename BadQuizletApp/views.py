from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, "homepage.html")

def createSet(request):
	return render(request, "create.html")

def viewAll(request):
	return render(request, "viewAll.html")

def random(request):
	return render(request, "random.html")

def viewCard(request):
	return render(request, "viewCard.html")