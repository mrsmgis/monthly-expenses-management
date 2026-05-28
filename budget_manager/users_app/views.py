from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def show(req):
    return render(req, "users_app/users.html")