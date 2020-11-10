from django.urls import path
from .views import navPageView
from .views import accountPageView
from .views import subscriptionsPageView
from .views import searchPageView


urlpatterns = [
    path("", navPageView, name="navigation"),    
    path("search/", searchPageView, name="search"),   
    path("subscriptions/", subscriptionsPageView, name="subscriptions"),  
    path("account/", accountPageView, name="account")    
]       