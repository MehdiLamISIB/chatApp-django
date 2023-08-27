from django.shortcuts import render
### On importe built-in lib de django
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate





def connect_user(request,user):
    pass

def home(request,user):
    return render(request,template_name="main.html",context={'user_name':user.name})





def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        ### Utilisateur existe
        pass
    else:
        ### On le redirige vers la page d'inscription
        pass
def logout_view(request):
    logout(request)