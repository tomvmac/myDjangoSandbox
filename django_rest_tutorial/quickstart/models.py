from django.db import models

# Create your models here.
class Car(models.Model):
	make = models.CharField(max_length=200)
	model = models.CharField(max_length=200)
	year = models.CharField(max_length=200)
	comments = models.CharField(max_length=200)

	class Meta:
		db_table = 'car'
