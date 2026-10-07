from rest_framework import serializers

from django.contrib.auth.models import User

from bookings.models import Appointments

from datetime import datetime

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

class AppointmentSerializer(serializers.ModelSerializer):

    doctor=serializers.StringRelatedField()
    class Meta:
        model=Appointments
        fields="__all__"
        read_only_fields=["id","token_number","appointment_time","created_at"]

    def validate(self,validated_data):
        appointment_date=validated_data.get("appoinment_date")
        doctor=validated_data.get("doctor")
        if appointment_date<datetime.today().date():
            raise serializers.ValidationError("date should be > cur date")
        last_appointment_object=Appointments.objects.filter(doctor=doctor,appointment_date=appointment_date)
        if last_appointment_object:
            if last_appointment_object.token_number==25:
                raise serializers.ValidationError("slot full...")
        
        return validated_data