from django.db import models

class UserInteraction(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)


