from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## pour créer le nouveau user
class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=User
        fields=("username","password","password2")
    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        if commit:
            user.save()
        else:
            print("ERROR USER CREATION")
        return user
    pass