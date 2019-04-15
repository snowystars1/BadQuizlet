from django.db import models

# Create your models here.

class Cards(models.Model):
	set_id = models.IntegerField(default=0)
	set_name = models.CharField(max_length=100)
	term = models.CharField(max_length = 200)
	definition = models.CharField(max_length = 400)
