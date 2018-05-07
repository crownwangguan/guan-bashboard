from django.shortcuts import render
from .models import Job


def index(request):
    menu = ['work', 'education', 'skills']
    return render(request, 'index.html', {'menu': menu})


def work(request):
    jobs = Job.objects.order_by('-start').all()
    for job in jobs:
        job.end = job.end if job.end else 'Present'
    return render(request, 'resume/jobs.html', {'jobs': jobs})