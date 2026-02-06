from django.urls import path
from Guest import views

app_name = "Guest"

urlpatterns = [
    path('Login/',views.Login,name="Login"),
    path('Index/',views.Index,name="Index"),
]