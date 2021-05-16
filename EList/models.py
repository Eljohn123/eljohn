from django.db import models

# Create your models here.
class List(models.Model):
	pass
class Item(models.Model):
	DiaId = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
	diary_name = models.TextField(default='')
	diary_date = models.TextField(default='')
	mood = models.TextField(default='')
	achi = models.TextField(default='')
	entry = models.TextField(default='')

