from django.shortcuts import render



from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from booking_v2.serializers import SignupSerializer

from booking_v2.serializers import AppointmentSerializer
from bookings.models import Appointments

from datetime import time,timedelta,datetime

from rest_framework import authentication,permissions

from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

 
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

class AppointmentListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
                        
    def get(self,request):
        qs=Appointments.objects.all()
        serializer_instance=AppointmentSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=AppointmentSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            doctor_id=cleaned_data.get("doctor")
            appointment_date=cleaned_data.get("appointment_date")
            last_appointment_object=Appointments.objects.filter(doctor=doctor_id,appointment_date=appointment_date).last()
            appointment_time=time(10,0)
            if last_appointment_object:
                cleaned_data["token_number"]=last_appointment_object.token_number+1
                next_appointment_date_time=datetime.combine(appointment_date,last_appointment_object.appointment_time)+timedelta(minutes=15)
                appointment_time=next_appointment_date_time.time()
            else:
                cleaned_data["token_number"]=1
            qs=Appointments.objects.create(**cleaned_data,appointment_time=appointment_time)
            serializer_instance=AppointmentSerializer(qs)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class AppointmentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=AppointmentSerializer
    queryset=Appointments.objects.all()