from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Logins

def index(request):
    dict_response = {}
    mymembers = Logins.objects.all().values()

    if request.method == 'POST' and 'login' in request.POST and request.POST['login'] and 'password' in request.POST and \
            request.POST['password']:
        for mymember in mymembers:
            if request.POST['login'] == mymember['login'] and request.POST['password'] == mymember['password']:
                dict_response['login'] = True
                break
            else:
                dict_response['login'] = False

    response = JsonResponse(dict_response)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
