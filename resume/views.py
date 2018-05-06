from django.shortcuts import render


def index(request):
    menu = ['work', 'education', 'skills']
    return render(request, 'resume/index.html', {'menu': menu})
