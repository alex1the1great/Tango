from django.shortcuts import render


def index(request):
    context = {
        'message': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, 'rango/index.html', context)


def about(request):
    return render(request, 'rango/about.html')
