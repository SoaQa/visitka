from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index/index.html')


def hello(request):
    return JsonResponse({"result": "ok"})
