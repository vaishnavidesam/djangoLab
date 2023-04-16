from django.urls import path

from.views import hello_msg

urlpatterns = [
    path("", hello_msg, name="home"),
]