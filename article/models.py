from django.db import models
from category.models import Category
from userprofile.models import UserProfile
#from django.utils import datetime


class Article(models.Model):
	id = models.AutoField(primary_key=True)
	category=models.ForeignKey(Category,default='1')
	language=models.CharField(max_length=32,default='c')
	noofslides=models.IntegerField(default='1')
	title=models.CharField(max_length=128,default='q')
	url=models.CharField(max_length=123,default='u')
	hastags=models.CharField(max_length=123,default='a')
	keywords=models.CharField(max_length=128,default='s')
	content=models.TextField()
	subheading=models.CharField(max_length=80,default='sh')
	reference = models.CharField(max_length=128,default='d')
	image=models.CharField(max_length=128,default='a')
	views=models.IntegerField(default='0')
	dateTime=models.DateField(auto_now=False, auto_now_add=False)
	postedby=models.ForeignKey(UserProfile,default='1')
	published=models.IntegerField(default='1')

	def __str__(self):
		self.title


# Create your models here.
