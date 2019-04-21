from django.db import models

# Create your models here.

class Sets(models.Model):
	set_name = models.CharField(max_length=100)

class Cards(models.Model):
	card_set = models.ForeignKey(Sets, on_delete=models.CASCADE)
	term = models.CharField(max_length = 200)
	definition = models.CharField(max_length = 400)
