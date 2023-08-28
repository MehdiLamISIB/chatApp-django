from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import ChatMessage

## pour créer le nouveau user
class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)   
    class Meta:
        model=User
        fields=("username","email","password1","password2")
    
    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        else:
            print("ERROR USER CREATION")
        return user
    pass

## Pour Récuprer les nouveaux message envoyés
class ChatMessageForm(forms.ModelForm):
    
    class Meta:
        model=ChatMessage
        ### On ne met pas dateMessage car il est généré automatiquement
        fields=["username","message"]