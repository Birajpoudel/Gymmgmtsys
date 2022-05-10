from django.shortcuts import redirect, render



def HOME(request):
    return render (request, 'home.html')

def BASE(request):
    return render (request, 'base.html')

