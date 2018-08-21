from django.shortcuts import render, get_object_or_404

from rest_framework import generics,status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from callapi.models import CallStart, CallEnd, CallRecord, PhoneBill
from callapi.serializers import (CallStartSerializer, CallEndSerializer, 
								CallRecordSerializer, PhoneBillSerializer)
from .billing import billing

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Call Starts': reverse('call-start', request=request, 
        						format=format),
        'Call Ends': reverse('call-end', request=request, 
        						format=format),
        'Call Records': reverse('call-records', request=request, 
        						format=format),
        'Telephone Bills': reverse('bills', request=request, 
        						format=format),
    })



class CallStartCreate(generics.ListCreateAPIView):
	queryset = CallStart.objects.all()
	serializer_class = CallStartSerializer

	def create(self, validated_data):
		try:
			call_id = validated_data.data['call_id']
			source = validated_data.data['source']
			destination = validated_data.data['destination']
			timestamp = validated_data.data['timestamp']
		except:
			raise serializers.ValidationError({
				"non_fields_error": [
					"All fields are required.",
					"Fields: source, destination, call_id, timestamp"
					]
				})
		else:
			source_number = ''.join(x for x in source if x.isdigit())
			destination_number = ''.join(x for x in destination if x.isdigit())
			serializer = CallStartSerializer(
				data={"source": source_number, "destination": destination_number, 
						"call_id": call_id, "timestamp": timestamp})
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CallEndCreate(generics.ListCreateAPIView):
	queryset = CallEnd.objects.all()
	serializer_class = CallEndSerializer

	def create(self, validated_data):
		try:
			print(validated_data.data)
			call_id = validated_data.data['call_id']
			timestamp = validated_data.data['timestamp']
		except:
			print(validated_data.data)
			raise serializers.ValidationError({
				"non_fields_error": [
					"All fields are required.",
					"Fields: call_id, timestamp"
					]
				})
		else:
			serializer = CallEndSerializer(data={"call_id": call_id, 
												"timestamp": timestamp})
			if serializer.is_valid():
				serializer.save()
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		finally:
			call = CallStart.objects.all()
			callend = CallEnd.objects.all()
			for start in call:
				for end in callend:
					if start.call_id == end.call_id:
						CallRecord.objects.create(
							destination=start.destination, 
							start_time=start.timestamp.time(), 
							start_date=start.timestamp.date(), 
							duration = end.timestamp - start.timestamp, 
							price = 30, 
							)


class CallRecordCreate(generics.ListCreateAPIView):
	queryset = CallRecord.objects.all()
	serializer_class = CallRecordSerializer


class PhoneBillCreate(generics.ListCreateAPIView):
	queryset = PhoneBill.objects.all()
	serializer_class = PhoneBillSerializer

	# def get(self, request):
	# 	number = self.request.query_params.get('subscriber_phone', None)
	# 	call = PhoneBill.objects.filter(subscriber_phone=number)
	# 	serializer = PhoneBillSerializer(call, many=True)
	# 	return Response(serializer.data, status=status.HTTP_200_OK)

