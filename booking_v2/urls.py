from django.urls import path

from booking_v2.views import SignupView

from booking_v2.views import AppointmentListCreateView
from booking_v2.views import AppointmentRetrieveUpdateDeleteView

urlpatterns=[
    path("signup/",SignupView.as_view()),

    path('appointment/',AppointmentListCreateView.as_view()),
    path('appointment/<int:pk>/',AppointmentRetrieveUpdateDeleteView.as_view()),

]