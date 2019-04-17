from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import CreateCardForm

from .models import Cards
# Create your views here.

def index(request):
	return render(request, "homepage.html")

def createSet(request):
	if request.method == 'POST':
		form = CreateCardForm(request.POST)
		if(form.is_valid()):
			set_name = form.cleaned_data['setName']
			card1front = form.cleaned_data['card1front']
			card1back = form.cleaned_data['card1back']
			addCard(set_name, card1front, card2front)
			return HttpResponseRedirect('SetCreated')
	else:
		form = CreateCardForm()
	return render(request, "create.html", {'form': form})

def viewAll(request):
	cards = Cards.objects.all()
	return render(request, "viewAll.html", {'cards':cards})
	#return render(request, "viewAll.html")

def random(request):
	return render(request, "random.html")

def viewCard(request):
	return render(request, "viewCard.html")

def createSet(request):
	return render(request, "create.html")


def addCard(setName, termName, definitionName):
	b = Cards.objects.create(set_name=setName, term = termName, definition=definitionName)
	b.save()

