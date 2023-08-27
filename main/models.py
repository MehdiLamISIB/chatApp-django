from django.db import models

class ChatMessage(models.Model):
    username=models.CharField(max_length=150)
    message=models.CharField(max_length=500)
    ### Permet d'ajouter la date quand créer
    dateMessage=models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return  f"{0}%{1}".format(self.username,self.dateMessage)