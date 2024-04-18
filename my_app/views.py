from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    with open('user_agents.txt', 'a') as file:
            file.write(request.META.get('HTTP_USER_AGENT', 'Unknown') + '\n')
    return render(request,'my_app/index.html')


def read(request):
    try:
        with open('user_agents.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "Le fichier des User-Agent n'existe pas ou n'a pas encore été créé."

    return HttpResponse(content, content_type='text/plain')