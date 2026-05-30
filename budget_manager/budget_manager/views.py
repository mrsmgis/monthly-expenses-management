from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, "layout.html")
def login(req):
    return render(req, 'registration/login.html')