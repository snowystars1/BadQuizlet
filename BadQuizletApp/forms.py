from django import forms

class CreateCardForm(forms.Form):
	setName = forms.CharField(label='Set Name', max_length=100)

	cardFronts = [None] * 10
	cardBacks = [None] * 10


	def __init__(self, *args, **kwargs):
		super(CreateCardForm, self).__init__(*args, **kwargs)

		for i in range(1, 11):
			self.fields['cardFront_%s' % i] = forms.CharField(label = 'Card ' + str(i) + ' Front', max_length = 100)
			self.fields['cardBack_%s' % i] = forms.CharField(label = 'Card ' + str(i) + ' Back', max_length = 100)

'''
	card1front = forms.CharField(label='Card 1 Front', max_length = 100)
	card1back = forms.CharField(label='Card 1 Back', max_length = 100)
	card2front = forms.CharField(label='Card 2 Front', max_length = 100)
	card2back = forms.CharField(label='Card 2 Back', max_length = 100)
	card3front = forms.CharField(label='Card 3 Front', max_length = 100)
	card3back = forms.CharField(label='Card 3 Back', max_length = 100)
	card4front = forms.CharField(label='Card 4 Front', max_length = 100)
	card4back = forms.CharField(label='Card 4 Back', max_length = 100)
	card5front = forms.CharField(label='Card 5 Front', max_length = 100)
	card5back = forms.CharField(label='Card 5 Back', max_length = 100)
	card6front = forms.CharField(label='Card 6 Front', max_length = 100)
	card6back = forms.CharField(label='Card 6 Back', max_length = 100)
	card7front = forms.CharField(label='Card 7 Front', max_length = 100)
	card7back = forms.CharField(label='Card 7 Back', max_length = 100)
	card8front = forms.CharField(label='Card 8 Front', max_length = 100)
	card8back = forms.CharField(label='Card 8 Back', max_length = 100)
	card9front = forms.CharField(label='Card 9 Front', max_length = 100)
	card9back = forms.CharField(label='Card 9 Back', max_length = 100)
	card10front = forms.CharField(label='Card 10 Front', max_length = 100)
	card10back = forms.CharField(label='Card 10 Back', max_length = 100)
	'''
	