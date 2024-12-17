from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import UserInteraction

# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")

#def home(request):
#    return render(request, "home.html")

def hello_api(request):
    return JsonResponse({"message": "Hello, World!"})

def create_interaction(request):
    interaction = UserInteraction(message="Hello, World!")
    interaction.save()
    return JsonResponse({"message": "Interaction created!", "id": interaction.id})

