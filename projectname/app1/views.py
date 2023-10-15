from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return HttpResponse("hello world....")



def display(request):
	return HttpResponse("je suis toujours là,merci de me contacter ce soir si vous voulez")
# Create your views here.

def exemple_view(request,parameter):
	return HttpResponse(f"le parametre que vous avez tapé est : {parameter}")
