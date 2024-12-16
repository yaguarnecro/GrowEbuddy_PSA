from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Note  # Assuming you have a Note model

# Create your views here.

class VpetListView(View):
    def get(self, request):
        # Logic to retrieve Vpets
        return JsonResponse({"message": "List of Vpets"})

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'  # Specify your template name
    context_object_name = 'notes'  # Name of the variable to be used in the template
