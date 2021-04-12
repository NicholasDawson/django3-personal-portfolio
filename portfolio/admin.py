from django.contrib import admin
from .models import *

"""
What models we want to show up in the admin dashboard
"""

admin.site.register(Project, ProjectAdmin)

