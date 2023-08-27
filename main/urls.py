from django.urls import path
from . import views


### Permet de lier les urls au views-model
urlpatterns = [
    #path("", views.homepage, name="homepage"),
    path("",views.home,name="home"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]