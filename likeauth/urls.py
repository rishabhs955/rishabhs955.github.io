from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', loginView, name="loginView"),
    path('register/', registerView, name="registerView"),
    path('logout/', logoutView, name="logoutView"),
    path('like/<int:id>/', like),
    path('dislike/<int:id>/', dislike),
]
