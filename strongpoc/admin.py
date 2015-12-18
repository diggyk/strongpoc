from django.contrib import admin
from . import models

admin.site.register(models.Team)
admin.site.register(models.ContactType)
admin.site.register(models.ServiceProvider)
admin.site.register(models.PointOfContact)
