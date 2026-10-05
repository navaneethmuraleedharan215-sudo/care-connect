from django.shortcuts import render



from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from booking_v2.serializers import SignupSerializer

from bookings.serializer import AppointmentSerializer

# Create your views here.
class SignupView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignupSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            user_object=User.objects.create_user(**cleaned_data)
            serializer_instance=SignupSerializer(user_object)
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class AppointmentSeralizerv2(seri)