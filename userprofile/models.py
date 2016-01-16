from django.db import models


class UserProfile(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=128,default='a')
	password=models.CharField(max_length=128,default='b')
	emailid=models.CharField(max_length=128,default='c')
	group=models.CharField(max_length=34,default='d')

	def __str__(self):
		self.username
# Create your models here.
