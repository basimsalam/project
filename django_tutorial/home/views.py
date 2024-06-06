from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("About Page")

def signup(request):
    return render(request,'register.html')

def registration(request):
    return HttpResponse("Registration Page")