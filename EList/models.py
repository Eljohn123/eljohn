from django.db import models
from datetime import datetime, date

# Create your models here.
class SignUp(models.Model):
	email = models.CharField(default='', max_length=250)
	phone_number = models.IntegerField(default='')
	username = models.CharField(default='',max_length=50)
	password = models.CharField(default='',max_length=50)
class Login(models.Model):
	username = models.CharField(default='',max_length=50)
	password = models.CharField(default='',max_length=50)
class List(models.Model):
	UserId = models.ForeignKey(Login, on_delete=models.CASCADE, default=None, null=True)
	diary_name = models.CharField(default='', max_length=100)
class Item(models.Model):
	DiaId = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
	diary_name = models.CharField(default='',max_length=100)
	diary_date = models.DateField(default='2021-05-20',auto_now_add=False, auto_now=False)
	mood = models.CharField(default='', max_length=150)
	achi = models.CharField(default='', max_length=150)
	entry = models.TextField(default='')
class Favorite(models.Model):
	DiaId = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
	diary_name = models.CharField(default='',max_length=100)
	favorite = models.CharField(default='',max_length=500)
	date_added = models.DateField(default='2021-05-20',auto_now_add=False, auto_now=False)
class ArchiveAuthenticate(models.Model):
	DiaId = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
	diary_name = models.CharField(default='',max_length=100)
	four_digit_passcode = models.CharField(default='', max_length=4)
class Archive(models.Model):
	ArchiveId = models.ForeignKey(ArchiveAuthenticate, on_delete=models.CASCADE, default=None)
	diary_name = models.CharField(default='',max_length=100)
	archive = models.CharField(default='',max_length=500)
	date_added = models.DateField(default='2021-05-20',auto_now_add=False, auto_now=False)
#class Login(models.Model):
#	username = models.CharField(default='', max_length())