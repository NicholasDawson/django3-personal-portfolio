from django.db import models
from django.contrib import admin

"""
Everytime you make a change to models it is called a migration.

They need to be migrated into the database.
"""


class Project(models.Model):
    title = models.CharField(max_length=100)    # 100 characters max
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')    # the location where the images are stored
    url = models.URLField(blank=True)   # blank means that the field is optional (this can be added to any field)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
