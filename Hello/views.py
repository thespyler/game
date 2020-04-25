from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
def HelloWorld(request):
	return HttpResponse("<html><body> <ul>Hello World <ul/></body> </html>")
# Create your views here.
