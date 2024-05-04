from django.db import models

# Create your models here.

class Technologies(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='portfolio/images/icons')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    descriptionSP = models.TextField(default=None, blank=True)
    descriptionEN = models.TextField(default=None, blank=True)
    image = models.ImageField(upload_to='portfolio/images/covers', default=None, blank=True)
    screen1 = models.ImageField(upload_to='portfolio/images/screens', default=None, blank=True)
    screen2 = models.ImageField(upload_to='portfolio/images/screens', default=None, blank=True)
    screen3 = models.ImageField(upload_to='portfolio/images/screens', default=None, blank=True)
    playStoreUrl = models.CharField(max_length=255, default=None, blank=True)
    appStoreUrl = models.CharField(max_length=255, default=None, blank=True)
    repositoryUrl = models.CharField(max_length=255, default=None, blank=True)
    technologies = models.ManyToManyField(Technologies)

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, default=None, blank=True)
    descriptionSP = models.TextField(default=None, blank=True)
    descriptionEN = models.TextField(default=None, blank=True)
    image = models.ImageField(upload_to='portfolio/images/profiles', default=None, blank=True)
    linkedinUrl = models.CharField(max_length=255, default=None, blank=True)
    githubUrl = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self):
        return self.name
