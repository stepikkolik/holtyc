from django.urls import path 

from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("send_email/", sendEmail, name="send_email"),
]