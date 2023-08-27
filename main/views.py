from django.shortcuts import render,redirect
### On importe built-in lib de django
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
###On import form.py
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


### PERMET DE RAJOUTER L'UTILISATEUR
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		##SI FORMULAIRE VALIDE
		if form.is_valid():
			print("LE FORM EST VALIDE")
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		else:
			###MONTRE LES ERREURS DU FORM
			print(form.error_messages)
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

### PERMET DE CONNECTER L'UTILISATEUR
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


### PERPMET DE SE DECONNECTER
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")


### MENU DE BASE POUR TEST
def homepage(request):
    return render(request,template_name="main.html")#,context={'user_name':user.name})





