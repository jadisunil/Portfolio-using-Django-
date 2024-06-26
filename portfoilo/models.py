from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField()

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(
        upload_to='about_images/', blank=True, null=True)  # Add this field

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField()
    linkedin_link = models.URLField(max_length=200)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.email


class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
