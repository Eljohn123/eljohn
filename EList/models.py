from django.db import models
from datetime import datetime, date

# Create your models here.
#class User(models.Model):
#	thebestinthewest  = models.CharField(default='', max_length=120)
class Login(models.Model):
	phone_number = models.CharField(default='', max_length=30)
	email = models.CharField(default='', max_length=250)
	username = models.CharField(default='',max_length=50)
	password = models.CharField(default='',max_length=50)
class Item(models.Model):
	#DiaId = models.ForeignKey(Login, on_delete=models.CASCADE, default=None)
	diary_name = models.CharField(default='',max_length=100)
	diary_date = models.DateTimeField(auto_now_add=True)
	mood = models.CharField(default='', max_length=150)
	achi = models.CharField(default='', max_length=150)
	entry = models.TextField(default='')

	def __str__(self):
		return self.diary_name + " " + self.diary_date

	class Meta:
		ordering = ['created']
         
	class Meta:  
		db_table = "EList"

class Favorite(models.Model):
	DiaId = models.ForeignKey(Login, on_delete=models.CASCADE, default=None)
	favorite = models.CharField(default='',max_length=500)
	date_added = models.DateField(default='2021-05-20',auto_now_add=False, auto_now=False)
class Archive(models.Model):
	DiaId = models.ForeignKey(Login, on_delete=models.CASCADE, default=None)
	four_digit_passcode = models.CharField(default='', max_length=4)
	archive = models.CharField(default='',max_length=500)
	date_added = models.DateField(default='2021-05-20',auto_now_add=False, auto_now=False)

#class Login(models.Model):
#	username = models.CharField(default='', max_length())