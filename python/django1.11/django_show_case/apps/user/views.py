import django
from django.shortcuts import render

def index(request):

    return django.http.response.JsonResponse({"result": "HelloWord"})
