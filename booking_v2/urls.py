from django.urls import path

from booking_v2.views import SignupView

urlpatterns=[
    path("signup/",SignupView.as_view()),

]