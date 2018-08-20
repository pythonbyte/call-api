from django.shortcuts import render, get_object_or_404

from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from callapi.models import CallStart, CallEnd, CallRecord, PhoneBill
from callapi.serializers import (CallStartSerializer, CallEndSerializer, 
								CallRecordSerializer, PhoneBillSerializer)


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
			source_number = validated_data.data['source_number']
			destination_number = validated_data.data['destination_number']
			call_pair = validated_data.data['call_pair_id']
			record = validated_data.data['record_timestamp']
		except:
			raise serializers.ValidationError({
				"non_fields_error": [
					"All fields are required."
					]
				})
		else:
			source_number = ''.join(x for x in source_number if x.isdigit())
			destination_number = ''.join(x for x in destination_number if x.isdigit())
			serializer = CallStartSerializer(
				data={"source_number": source_number, "destination_number": destination_number, 
						"call_pair_id": call_pair, "record_timestamp": record})
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CallEndCreate(generics.ListCreateAPIView):
	queryset = CallEnd.objects.all()
	serializer_class = CallEndSerializer

	def create(self, validated_data):
		try:
			call_pair = validated_data.data['call_pair_id']
			record_end_timestamp = validated_data.data['record_end_timestamp']
		except:
			raise serializers.ValidationError({
				"non_fields_error": [
					"All fields are required."
					]
				})
		else:
			serializer = CallEndSerializer(data={"call_pair_id": call_pair, "record_end_timestamp": record_end_timestamp})
			if serializer.is_valid():
				serializer.save()
			return Response(serlializer.errors, status=status.HTTP_400_BAD_REQUEST)
		finally:
			call = CallStartRecord.objects.all()
			callend = CallEndRecord.objects.all()
			for start in call:
				for end in callend:
					if start.call_pair_id == end.call_pair_id:
						CallRecord.objects.create(destination=start.destination_number, 
							call_start_time=start.record_timestamp.time(), 
							call_start_date=start.record_timestamp.date(), 
							call_duration = end.record_end_timestamp - start.record_timestamp, 
							call_price = 200, 
							bill_id=1)







class CallRecordCreate(generics.ListCreateAPIView):
	queryset = CallRecord.objects.all()
	serializer_class = CallRecordSerializer


class TelephoneBillCreate(generics.ListCreateAPIView):
	queryset = PhoneBill.objects.all()
	serializer_class = PhoneBillSerializer

	def get(self, request):
		number = self.request.query_params.get('subscriber_phone', None)
		call = TelephoneBill.objects.filter(subscriber_phone=number)
		serializer = PhoneBillSerializer(call, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

