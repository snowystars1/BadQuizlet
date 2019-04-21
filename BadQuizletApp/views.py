from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import CreateCardForm

from .models import Cards
from .models import Sets
#setID=0
# Create your views here.

def index(request):
	return render(request, "homepage.html")

def createSet(request):
	#global setID
	#setID=setID+1
	if request.method == 'POST':
		form = CreateCardForm(request.POST)
		if(form.is_valid()):
			#add to Set table
			card_set = addSet(form.cleaned_data['setName'])
			term = ''
			for name, value in form.cleaned_data.items():
				if name.startswith('cardFront_'):
					print(form.fields[name].label, value)
					print(name)
				if term == '':
					term = value
				else:
					#addCard(setID, form.cleaned_data['setName'], term, value)
					addCard(card_set, term, value)
					term = ''
			return HttpResponseRedirect('SetCreated')
	else:
		form = CreateCardForm()
	return render(request, "create.html", {'form': form})

def setCreated(request):
	return render(request, "setCreated.html")

def viewAll(request):
	#cards = Cards.objects.all()
	sets = Sets.objects.all()
	return render(request, "viewAll.html", {'sets':sets})

#view single set
def viewSet(request, setID):
	myset =Sets.objects.filter(id=setID)
	return render(request, "viewSet.html", {'myset':myset})

def random(request):
	return render(request, "random.html")

def viewCard(request):

	return render(request, "viewCard.html")

def addCard(set_name, termName, definitionName):
	c = Cards.objects.create(card_set=set_name, term = termName, definition=definitionName)
	print(c)
	c.save()

def addSet(setName):
	s = Sets.objects.create(set_name=setName)
	print(s)
	s.save()
	return s