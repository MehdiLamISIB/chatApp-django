# Image de base pour le conteneur, derniere version de Python
FROM python:latest

### ENV est différent de ARG !!!
## ARG nécessite de rajouter des arguments
## Dans les lignes de commandes, ce qui n'est pas utile dans mon cas
## /home/app/webapp ---> dossier racine de l'application django dans le conteneur
ENV DockerDir=/home/app/webapp

## On créer le dossier dans /home/app/webapp
RUN mkdir -p ${DockerDir}

# On place le programme dans ce repertoire
WORKDIR ${DockerDir}


### COPY est plus sûr que ADD
### car ADD ajoute aussi tar.gz (fichier compress)
### Docker recommande d'utiliser COPY
# COPY <src> <dest>
COPY . /${DockerDir}

# Rajoute les dépendences qui sont dans le fichier requirement.txt
RUN pip install -r requirement.txt

# Installation de crispy-forms avec bootstrap 5
RUN pip install django-crispy-forms
RUN pip install crispy-bootstrap5

# Ecoute sur le port 8000 où l'app tourne dans le conteneur
EXPOSE 8000

### RUN VS CMD
### RUN fait partie du processus de création de l'image
### CMD est appellé quand l'image tourne dans le conteneur

# Commande pour faire tourner l'application/serveur dans le conteneur
CMD python3 manage.py runserver 0:8000


#------------------------------------------------
# COMMANDE A FAIRE DANS LE TERMINAL
#------------------------------------------------
#
## CREER L'IMAGE (Dockerfile)
# docker build . -t image_name
# -t : permet de dire référencer image_name
#
## TOURNE L'IMAGE DANS UN CONTENEUR
# docker run image_name
#
# 
## TOURNE L'IMAGE DANS UN CONTENEUR AVEC PORT 80
# docker run --name container_name -p 8000:8000 image_names 
#
#
## ARRETER CONTENEUR
# docker stop 
#
## LISTE ET DONNE DES INFOS SUR LES CONTENEURS
# docker ps
#
## SUPPRIMER LE CONTENEUR
# docker rm container_names 
#
#
#
## LISTER LES IMAGES
# docker images
#
## SI JE VEUX SAUVEGARDER MES INFOS DE DB
## JE DOIS UTILISER DOCKER VOLUME
#
#----------------------------------------------------------------
# DEFINITIONS
#----------------------------------------------------------------
#
## CONTENEUR:
# Un conteneur est un environnement isolé et léger qui contient
# ce que mon application a besoin pour fonctionner (fichier,librairies,dépendances).
# Ces conteneurs sont isolé et indépendant de l'OS, les rendant portables,
# fonctionant de la même manière sur différent environnements.
#
#
## IMAGE:
# L'image contient les instructions nécessaire pour construire et exécuter l'application
# dans le conteneur. Elle peuvent être executé peu importe le système tant qu'il docker
# peut y tourner. Elle sont immuables, c'est à dire qu'une fois qu'elles on été crée elle ne
# peuvent pas être modifié. Pour cela il faut modifier le Dockerfile.
#
#
#
#
#

