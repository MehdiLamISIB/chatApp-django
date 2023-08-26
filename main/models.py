from django.db import models

## Creation des blogs dans l'accueil
class Blog(models.Model):
    blog_titre=models.CharField(max_length=50)
    auteur=models.CharField(max_length=50)
