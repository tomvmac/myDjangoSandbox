# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello Tom!")

def about(request):
	return HttpResponse("Rango says here's the about page.")    
