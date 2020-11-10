from django.http import HttpResponse

def loginPageView(request) :
    return HttpResponse('Login Page!')  