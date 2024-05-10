from django.shortcuts import render
from .models import *

# Create your views here.

def index(request, email):
    if not email:
        return render(request, '404.html')
    else:
        try:
            profile = Profile.objects.get(email=email)
        except:
            return render(request, '404.html')

        projects = Project.objects.filter(developer=profile)

        context = {
            'profile': profile,
            'projects': projects
        }

        return render(request, 'index.html', context)

def empty(request):
    return render(request, '404.html')
