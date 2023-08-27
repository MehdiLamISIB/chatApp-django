from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## pour créer le nouveau user
class NewUserForm(UserCreationForm):
    