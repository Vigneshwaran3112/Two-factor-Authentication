from django.db import models

# Create your models here.
class data(models.Model):
	"""docstring for data"""
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	password = models.CharField(max_length=8)
	twoauth = models.CharField(max_length=10)

	class Meta:
		db_table = 'data'