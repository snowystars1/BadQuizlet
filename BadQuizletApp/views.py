from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import CreateCardForm

# Create your views here.

def index(request):
	return render(request, "homepage.html")

def createSet(request):
	if request.method == 'POST':
		form = CreateCardForm(request.POST)
		if(form.is_valid()):
			print(form.cleaned_data['card1back'])
			return HttpResponseRedirect('SetCreated')
	else:
		form = CreateCardForm()
	return render(request, "create.html", {'form': form})

def setCreated(request):
	return render(request, "setCreated.html")

def viewAll(request):

	return render(request, "viewAll.html")

def random(request):
	return render(request, "random.html")

def viewCard(request):
	return render(request, "viewCard.html")