from django.urls import path,include
from . import views


### Permet de lier les urls au views-model
urlpatterns = [
    #path("", views.homepage, name="homepage"),
    path("",views.homepage,name="homepage"),
    path("forum",views.forum,name="forum"),
    path("forum/message",views.sendMessage_Forum,name="sendMessage_Forum"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    #### Portail special pour supprimer message
    path('deleteALL123456789',views.delete_message,name="delete_message"),
    path('getNewMessages',views.getNewMessage,name="getNewMessage"),
]