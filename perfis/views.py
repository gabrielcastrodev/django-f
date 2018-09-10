from django.shortcuts import render
from perfis.models import Perfil
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def exibir(request, id):
	perfil = Perfil.objects.get(id=id)
	return render(request, 'perfil.html', {'perfil':perfil})

def convidar(requeste, id):
	pass
