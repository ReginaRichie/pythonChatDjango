from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


def index(request):
    response = JsonResponse({"login": True, })
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
