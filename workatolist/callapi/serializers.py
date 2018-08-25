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
			raise serializers.ValidationError("Source number must be different to destination number")
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

	def get_price(self, instance):
		return f'R$ {instance.price}'

	class Meta:
		model = CallRecord
		exclude = ['source', 'bill','id']


class PhoneBillSerializer(serializers.ModelSerializer):
	subscriber= serializers.CharField(min_length=10, max_length=11, required=True)
	period = serializers.SerializerMethodField()
	total = serializers.CharField(max_length=10)
	bills = serializers.SerializerMethodField()
	

	def get(self, instance, validated_data):
		print(self, instance, validated_data, validated_data.data)
		pass


	def get_bills(self, instance):
		if instance.period == None:
			now = datetime.now()
			month = now.month - 1
			year = now.year
			
		else:
			month = instance.period.month
			year  = instance.period.year
		call = CallRecord.objects.filter(source=instance.subscriber, start_date__month=month, start_date__year=year)
		ser = CallRecordSerializer(call, many=True)
		return ser.data

	def get_period(self, instance):

		if instance.period == None:
			now = datetime.now()
			month = now.month - 1
			year = now.year
		else:
			month = instance.period.month
			year  = instance.period.year
		return f"{month}/{year}"

	def save(self):
		period = self.validated_data['period']
		print(period)
		article = self.validated_data['article']

	class Meta:
		model = PhoneBill
		exclude = ['id']
