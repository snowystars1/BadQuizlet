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
			term = ''
			for name, value in form.cleaned_data.items():
				if name.startswith('cardFront_'):
					print(form.fields[name].label, value)
					print(name)
				if term == '':
					term = value
				else:
					addCard(form.cleaned_data['setName'], term, value)
					term = ''
			return HttpResponseRedirect('SetCreated')
	else:
		form = CreateCardForm()
	return render(request, "create.html", {'form': form})

def setCreated(request):
	return render(request, "setCreated.html")

def viewAll(request):
	cards = Cards.objects.all()
	return render(request, "viewAll.html", {'cards':cards})

def viewSet(request):
	cards = Cards.objects.all()
	return render(request, "viewSet.html", {'cards':cards})

def random(request):
	return render(request, "random.html")

def viewCard(request):

	return render(request, "viewCard.html")

def addCard(setName, termName, definitionName):
	b = Cards.objects.create(set_name=setName, term = termName, definition=definitionName)
	b.save()