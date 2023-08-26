from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello page is working<h1>")

def chatPage(request,*args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")