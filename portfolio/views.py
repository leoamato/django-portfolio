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

        if profile.linkedinUrl:
            githubIcon = Technologies.objects.get(name="Github")
        else:
            githubIcon = None

        if profile.githubUrl:
            linkedinIcon = Technologies.objects.get(name="Linkedin")
        else:
            linkedinIcon = None

        context = {
            'profile': profile,
            'projects': projects,
            'linkedinIcon': linkedinIcon.icon,
            'githubIcon': githubIcon.icon
        }
        
        print("CONTEXT: ", context)

        return render(request, 'index.html', context)

def empty(request):
    return render(request, '404.html')
