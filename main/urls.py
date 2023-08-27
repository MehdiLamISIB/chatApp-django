from django.urls import path
from main import views as main_views
from django.contrib.auth.views import LoginView, LogoutView
### ON UTILISE TEMPLATE CE QUE DJANGO DONNE DEJA
urlpatterns = [
    path("",main_views.chatPage,name="chat-page"),
    path("auth/login/",LoginView.as_view
         (template_name="main/LoginPage.html"),name="login-user"),
    path("auth/logout/",LoginView.as_view(), name="logout-user"),
]
