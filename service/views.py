from django.shortcuts import render
from .models import Service, TeamMember, Event, HappyClients, AboutUs, Segmentation

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




def about(request):
    about_us = AboutUs.objects.all()
    segment = Segmentation.objects.all()
    context = {
        'abouts': about_us,
        'segments': segment
    }

    return render(request, 'about.html', context)


def contact_us(request):
    return render(request, 'contact_us.html')





