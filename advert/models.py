from django.db import models


class Advert(models.Model):
	id=models.AutoField(primary_key=True)
	client=models.CharField(max_length=128,default='a')
	formate=models.IntegerField(default='1')
	slot=models.IntegerField(default='909012')
	page=models.CharField(max_length='40',default='article')
	width=models.IntegerField(default='100')
	height=models.IntegerField(default='100')
	min_width=models.IntegerField(default='90')
	min_height=models.IntegerField(default='90')
	display=models.CharField(max_length=67,default='a')
	published=models.IntegerField(default='1')


	def __str__(self):
		self.slot
# Create your models here.
