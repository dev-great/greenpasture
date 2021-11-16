from django.db import models
from datetime import datetime
from django.utils.timezone import timezone


# Create your models here.

class store(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	price = models.IntegerField()
	book_url = models.CharField(max_length=200)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
	is_published = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now , blank=True)


	def __str__(self):
		return self.title;
