from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer
from staff_v2.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class DoctorListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request):
        qs=Doctor.objects.all()
        serializer_instance=DoctorSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Doctor.objects.create(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)

class DoctorRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
        qs=Doctor.objects.get(id=pk)
        serializer_instance=DoctorSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Doctor.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)

class UserCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            #User.objects.create_superuser(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)