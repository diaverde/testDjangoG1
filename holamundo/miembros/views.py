import email
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

from .models import Member


def index(request):
    return HttpResponse("Hola, mundo")

def new(request):
    print("Method: ", request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #print(data)
            #print(type(data))
            member = Member(
                id = data['doc'],
                name = data['nombre'],
                email = data['email']
            )
            member.save()
            return HttpResponse("Está registrando datos.")
        except:
            return HttpResponseBadRequest("Error en los datos enviados.")
    else:
        return HttpResponseNotAllowed(["POST"], "Método inválido.")

