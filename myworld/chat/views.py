from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import loader


def index(request):
    dict_response = {}

    if request.method == 'POST':
        if 'login' in request.POST and request.POST['login'] and 'password' in request.POST and request.POST['password']:
            if request.POST['login'] == 'regina':
                dict_response['login'] = True
            else:
                dict_response['login'] = False

            if request.POST['password'] == '123':
                dict_response['password'] = True
            else:
                dict_response['password'] = False


    response = JsonResponse(dict_response)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

