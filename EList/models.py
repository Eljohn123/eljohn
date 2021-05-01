from django.db import models

# Create your models here.
class List(models.Model):
	pass
class Item(models.Model):
	DiaId = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
	text = models.TextField(default='')


