from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Home Page!')  