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

# Ecoute sur le port 8000 où l'app tourne dans le conteneur
EXPOSE 8000

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
## TOURNE L'IMAGE
# docker run image_name
#
#
# TOURNE l'APPLICATION PORT 80
# docker run -p 8000:8000 image_names 
#
## SI JE VEUX SAUVEGARDER MES INFOS DE DB
## JE DOIS AVOIR UTILISER DOCKER VOLUME
#
#
#
#
#
#



