from django.db import models

class Chat_message(models.Model):
    username=models.CharField(max_length=150)
    message=models.CharField(max_length=500)
    ### Permet d'ajouter la date quand créer
    date_message=models.DateTimeField(auto_now=False, auto_now_add=True)