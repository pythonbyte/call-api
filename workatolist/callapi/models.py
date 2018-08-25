from django.db import models
from datetime import datetime

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


class PhoneBill(models.Model):
	subscriber =  models.CharField(max_length=11, unique=True)
	period	= models.DateField(blank=True, null=True)
	total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)


class CallRecord(models.Model):
	id = models.AutoField(primary_key=True)
	source 	= models.CharField(max_length=11, null=True)
	destination = models.CharField(max_length=11)
	start_date 	= models.DateField(null=True, blank=True)
	end_date 	= models.DateField(null=True, blank=True)
	start_time 	= models.TimeField(null=True, blank=True)
	duration 	= models.DurationField(null=True, blank=True)
	price 	= models.DecimalField(max_digits=8, decimal_places=2, null=True)
	bill 	= models.ForeignKey(PhoneBill, on_delete=models.CASCADE, null=True, blank=True, related_name="bills")

