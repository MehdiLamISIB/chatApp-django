from django.shortcuts import render,redirect
### On importe built-in lib de django
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm



### PERMET DE RAJOUTER L'UTILISATEUR
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def connect_user(request,user):
    pass

def home(request):
    return render(request,template_name="main.html")#,context={'user_name':user.name})





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