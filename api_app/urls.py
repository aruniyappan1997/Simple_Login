from django.urls import path 
from .views import SignUp, Signin, Home, Delete, Update

urlpatterns = [
    path('', Signin, name="sign-in"),
    path('sign-up/', SignUp, name="sign-up"),
    path('home/', Home, name="home"),
    path('delete/<int:id>', Delete, name="delete"),
    path('update/<int:id>', Update, name="update"),
]