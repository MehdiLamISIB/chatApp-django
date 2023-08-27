from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## pour créer le nouveau user
class NewUserForm(UserCreationForm):
    #username = forms.CharField(label='username', min_length=5, max_length=125) 
    email=forms.EmailField(required=True)
    #password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)    
    class Meta:
        model=User
        fields=("username","email","password1","password2")
    
    def save(self,commit=True):
        #user=User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['email'],self.cleaned_data['password1'])
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        #user.password=self.cleaned_data["password1"]
        #user.username=self.cleaned_data["username"]
        if commit:
            user.save()
        else:
            print("ERROR USER CREATION")
        return user