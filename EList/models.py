from django.db import models
from datetime import datetime, date

# Create your models here.
class List(models.Model):
	diary_name = models.CharField(default='', max_length=100)
class Item(models.Model):
	DiaId = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
	diary_name = models.CharField(default='',max_length=100)
	diary_date = models.DateField(default='2021-05-20',auto_now_add=False, auto_now=False, blank=True)
	mood = models.CharField(default='', max_length=150)
	achi = models.CharField(default='', max_length=150)
	entry = models.TextField(default='')
class SignUp(models.Model):
	email = models.CharField(default='', max_length=250)
	username = models.CharField(default='',max_length=50)
	password = models.CharField(default='',max_length=50)
class Login(models.Model):
	username = models.CharField(default='',max_length=50)
	password = models.CharField(default='',max_length=50)
class Favorite(models.Model):
	favorite = models.CharField(default='',max_length=500)
class Archive(models.Model):
	archive = models.CharField(default='',max_length=500)
#class Login(models.Model):
#	username = models.CharField(default='', max_length())