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

def read(request):
    if request.method == 'GET':
        members = Member.objects.all()
        allMembersData = []
        for x in members:
            memberData = {"documento": x.id, "nombre": x.name, "correo": x.email}
            allMembersData.append(memberData)
        #print(json.dumps(allMembersData))
        resp = HttpResponse()
        resp.headers['Content-Type'] = 'text/json'
        resp.content = json.dumps(allMembersData)
        return resp
    else:
        return HttpResponseNotAllowed(["GET"], "Método inválido.")