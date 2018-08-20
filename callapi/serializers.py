from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from callapi.models import CallStart, CallEnd, CallRecord, PhoneBill



class CallStartSerializer(serializers.ModelSerializer):
	record_type = serializers.SerializerMethodField()
	source_number = serializers.CharField(min_length=10, max_length=11, required=True)
	destination_number = serializers.CharField(min_length=10, max_length=11, required=True)

	

	def get_record_type(self, obj):
		obj.record_type = 'start'
		return obj.record_type

	def validate(self, data):
		source_number = data['source_number']
		destination_number = data['destination_number']
		if source_number == destination_number:
			raise serializers.ValidationError("Source number must be different to destination number")
		return data



	class Meta:
		model = CallStart
		fields = '__all__'


class CallEndSerializer(serializers.ModelSerializer):
	record_end_type	 = serializers.SerializerMethodField()

	def get_record_end_type	(self, instance):
		instance.record_end_type = 'end'
		return instance.record_end_type	

	class Meta:
		model = CallEnd
		fields = ('__all__')



class CallRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = CallRecord
		fields = '__all__'


class PhoneBillSerializer(serializers.ModelSerializer):
	subscriber_phone = serializers.CharField(min_length=10, max_length=11, required=True)
	reference_period = serializers.CharField(max_length=10)
	bill = CallRecordSerializer(many=True)
	

	class Meta:
		model = PhoneBill
		fields = '__all__'
