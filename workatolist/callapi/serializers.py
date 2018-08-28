from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from callapi.models import CallStart, CallEnd, CallRecord, PhoneBill
from datetime import datetime, date


class CallStartSerializer(serializers.ModelSerializer):
	record_type = serializers.SerializerMethodField()
	source = serializers.CharField(min_length=10, max_length=11, required=True)
	destination = serializers.CharField(min_length=10, max_length=11, required=True)

	def get_record_type(self, obj):
		obj.record_type = 'start'
		return obj.record_type

	def validate(self, data):
		source_number = data['source']
		destination_number = data['destination']
		if source_number == destination_number:
			raise serializers.ValidationError(
				"Source number must be different to destination number"
				)
		return data

	class Meta:
		model = CallStart
		exclude = ['call_type',]



class CallEndSerializer(serializers.ModelSerializer):
	record_type	 = serializers.SerializerMethodField()

	def get_record_type	(self, instance):
		instance.record_end_type = 'end'
		return instance.record_end_type	

	class Meta:
		model = CallEnd
		exclude = ['call_type']



class CallRecordSerializer(serializers.ModelSerializer):
	price = serializers.SerializerMethodField()
	duration = serializers.SerializerMethodField()

	def get_price(self, instance):
		return f'R$ {instance.price}'.replace('.',',')

	def get_duration(self, instance):
		return instance.duration.__str__()

	class Meta:
		model = CallRecord
		fields = ['destination', 'start_date', 'start_time', 'duration', 'price']


class PhoneBillSerializer(serializers.ModelSerializer):
	subscriber= serializers.CharField(min_length=10, max_length=11, required=True)
	period = serializers.SerializerMethodField()
	total = serializers.SerializerMethodField()
	bills = serializers.SerializerMethodField()
	

	def get_bills(self, instance):
		if instance.period == None:
			now = datetime.now()
			month = now.month - 1
			year = now.year
			
		else:
			month = instance.period.month
			year  = instance.period.year

		call = CallRecord.objects.filter(source=instance.subscriber, 
										end_date__month=month, 
										end_date__year=year)
		serializer = CallRecordSerializer(call, many=True)
		return serializer.data

	def get_period(self, instance):
		if instance.period == None:
			now = datetime.now()
			month = now.month - 1
			year = now.year
		else:
			month = instance.period.month
			year  = instance.period.year
		return f"{month}/{year}"


	def get_total(self,instance):
		if instance.period == None:
			now = datetime.now()
			month = now.month - 1
			year = now.year
			
		else:
			month = instance.period.month
			year  = instance.period.year

		calls = CallRecord.objects.filter(source=instance.subscriber, 
											end_date__month=month, 
											end_date__year=year)
		total = 0
		for call in calls:
			total = total + call.price
		return f"R$ {total}".replace('.',',')

	class Meta:
		model = PhoneBill
		exclude = ['id']
