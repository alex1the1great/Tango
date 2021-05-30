from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'message': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, 'rango/index.html', context)


def about(request):
    message = 'Rango says here is the about page.<br><a href=/rango/>Home</a>'
    return HttpResponse(message)