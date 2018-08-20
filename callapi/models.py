from django.db import models


class CallStart(models.Model):
	id = models.AutoField(primary_key=True)
	call_id 	= models.PositiveIntegerField(unique=True)
	call_type 	= models.CharField(max_length=10, blank=False)
	timestamp = models.DateTimeField(blank=False)
	source 	= models.CharField(max_length=11)
	destination = models.CharField(max_length=11)

	def __str__(self):
		return "{}".format(self.call_id)	

class CallEnd(models.Model):
	id = models.AutoField(primary_key=True)
	call_id = models.PositiveIntegerField(unique=True)
	call_type = models.CharField(max_length=10,blank=False)
	timestamp = models.DateTimeField(blank=False)

	def __str__(self):
		return "{}".format(self.call_id)

class CallRecord(models.Model):
	id = models.AutoField(primary_key=True)
	destination = models.CharField(max_length=11)
	start_date = models.DateField(null=True, blank=True)
	start_time = models.TimeField(null=True, blank=True)
	duration 	= models.DurationField(null=True, blank=True)
	price 	= models.DecimalField(max_digits=8, decimal_places=2)

class PhoneBill(models.Model):
	subscriber =  models.CharField(max_length=11)
	period	= models.DateField(blank=False)
	total = models.DecimalField(max_digits=8, decimal_places=2)
	records = models.CharField(max_length=1000)