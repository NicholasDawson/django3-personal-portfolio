from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
