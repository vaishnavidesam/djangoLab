from django.shortcuts import render
from django.http import JsonResponse

def hello_msg(request):
    return JsonResponse({"Name": "Hello World!"})
# Create your views here.
