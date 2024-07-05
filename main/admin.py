from django.contrib import admin
from . import models

admin.site.register(models.News)
admin.site.register(models.NewsImg)
admin.site.register(models.NewsVideo)
admin.site.register(models.Comment)
admin.site.register(models.Athor)


