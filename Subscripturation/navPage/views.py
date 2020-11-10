from django.http import HttpResponse

def navPageView(request) :
    return HttpResponse('Navigation Page!')
    
def searchPageView(request) :
    return HttpResponse('Search Page!')

def subscriptionsPageView(request) :
    return HttpResponse('List of Subscriptions Page')

def accountPageView(request) :
    return HttpResponse('Account Information Page!')