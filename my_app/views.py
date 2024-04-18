from django.shortcuts import render
from django.http import JsonResponse
from .models import Agent
# Create your views here.

def index(request):
    nom =request.META.get('HTTP_USER_AGENT', 'Unknown')
    agent = Agent(nom=nom)
    agent.save() 
    return render(request,'my_app/index.html')


def read(request):
    agents = Agent.objects.values_list('nom', flat=True)
    agents_list = [agent for agent in agents]
    return JsonResponse(agents_list, safe=False)