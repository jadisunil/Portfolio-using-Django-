from django.contrib import admin
from .models import Project, About, WorkExperience, Contact

# Register your models here.
admin.site.register(Project)
admin.site.register(About)
admin.site.register(WorkExperience)
admin.site.register(Contact)
