from django.shortcuts import render


def index(request):
    menu = ['home', 'work', 'education', 'skills']
    return render(request, 'resume/index.html', {'menu': menu})
