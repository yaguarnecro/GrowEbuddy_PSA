from django.contrib import admin
from .models import UserInteraction, TodoItem  # Import the models

# Register your models here.
admin.site.register(UserInteraction)  # Register UserInteraction model
admin.site.register(TodoItem)          # Register TodoItem model
