from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse

from .models import Cards
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

def createSet(request):
	return render(request, "create.html")


def addCard(setName, termName, definitionName):
	b = Cards.objects.create(set_name=setName, term = termName, definition=definitionName)
	b.save()