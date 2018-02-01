from django.shortcuts import render


def index(request):
    context = dict(
        message='Hello World',
    )
    return render(request, 'index.haml', context)
