from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from callapi.views import *

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'


urlpatterns = [
	path('', api_root),
    path('call-start/', CallStartCreate.as_view(), name='call-start'),
    path('call-end/', CallEndCreate.as_view(), name='call-end'),
    path('call-records/', CallRecordCreate.as_view(), name='call-records'),
    path('bills/', PhoneBillCreate.as_view(), name='bills')
]

urlpatterns = format_suffix_patterns(urlpatterns)