from django.db import models


class Category(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50,default='a')
	keywords=models.CharField(max_length=50,default='a')
	
	def __str__(self):
		self.name
# Create your models here.
