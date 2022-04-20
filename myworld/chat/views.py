from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Logins

def index(request):
    dict_response = {}
    mymembers = Logins.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["login"]
    # print(output)
    
    if request.method == 'POST':
        if 'login' in request.POST and request.POST['login'] and 'password' in request.POST and request.POST['password']:
            if request.POST['login'] == 'regina' and request.POST['password'] == '1234':
                dict_response['login'] = True
            else:
                dict_response['login'] = False

    response = JsonResponse(dict_response)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    #return response, output
    return output
