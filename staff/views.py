from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from staff.models import Doctor


# Create your views here.
class DoctorListCreateView(APIView):
    def get(self,request):
        qs=Doctor.objects.all().values()
        doctors_list=list(qs)
        return Response(data=doctors_list)

    def post(self,request):
        form_data=request.data
        Doctor.objects.create(**form_data)
        return Response(data={"message":"created..."})

class DoctorRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
        qs=Doctor.objects.filter(id=pk).values()
        doctor_list=list(qs)
        return Response(data=doctor_list)

    def put(self,request,pk=None):
        form_data=request.data
        Doctor.objects.filter(id=pk).update(**form_data)
        return Response(data={"message":"updated..."})

    def delete(self,request,pk=None):
        Doctor.objects.get(id=pk).delete()
        return Response(data={"message":"deleted...."})


