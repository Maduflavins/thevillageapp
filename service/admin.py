from django.contrib import admin
from .models import Service, TeamMember, Event, HappyClients

# Register your models here.

admin.site.register(Service)
admin.site.register(TeamMember)
admin.site.register(Event)
admin.site.register(HappyClients)
