from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookoe, candy, cupcake"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says hey there partner")
