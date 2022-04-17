from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import loader


def index(request):
    dict_response = {}

    if request.method == 'POST':
        if 'login' in request.POST and request.POST['login']:
            dict_response['login'] = request.POST['login']

    response = JsonResponse(dict_response)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

