from django.shortcuts import render
from .models import Service, TeamMember, Event, HappyClients

# Create your views here.

def index(request):
    services = Service.objects.all()
    teammembers = TeamMember.objects.all()
    clients = HappyClients.objects.all()

    context = {
        'services': services,
        'teamembers': teammembers,
        'clients': clients
    }

    return render(request, 'index.html', context)





