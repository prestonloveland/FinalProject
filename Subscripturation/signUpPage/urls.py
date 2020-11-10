from django.urls import path
from .views import signUpPageView

urlpatterns = [
    path("", signUpPageView, name="signUp")    
] 