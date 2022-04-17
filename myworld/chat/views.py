from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import loader


def index(request):
    response = JsonResponse({"login": True, 'method': request.method})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

    # response = requests.get('http://ev-gen.ru/ReginaRichie/')
    # Вывод кода
    # print(response.status_code)
    # Вывод ответа, полученного от сервера API
    # print(response.json())
