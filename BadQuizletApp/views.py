from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import CreateCardForm

from .models import Cards
from .models import Sets

# Create your views here.

def index(request):
	return render(request, "homepage.html")

def createSet(request):
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
					addCard(card_set, term, value)
					term = ''
			return HttpResponseRedirect('SetCreated')
	else:
		form = CreateCardForm()
	return render(request, "create.html", {'form': form})

def setCreated(request):
	return render(request, "setCreated.html")

def viewAll(request):
	sets = Sets.objects.all()
	return render(request, "viewAll.html", {'sets':sets})

#view cards of single set
def viewSet(request, setID):
	myset =Sets.objects.filter(id=setID)
	cards = Cards.objects.filter(card_set__in=myset)
	return render(request, "viewSet.html", {'cards':cards})

def random(request):
	randomSet = Sets.objects.order_by('?')[:1] #apparently inefficient, consider doing something else
	cards = Cards.objects.filter(card_set__in=randomSet)
	return render(request, "random.html", {'cards':cards})

def viewCard(request):
	return render(request, "viewCard.html")

def addCard(set_name, termName, definitionName):
	c = Cards.objects.create(card_set=set_name, term = termName, definition=definitionName)
	c.save()

def addSet(setName):
	s = Sets.objects.create(set_name=setName)
	s.save()
	return s