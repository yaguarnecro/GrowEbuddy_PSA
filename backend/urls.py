from django.urls import path, include

print("Loading main.urls (from backend urls.py (x_x))")  # Debugging line

urlpatterns = [
    path('api/v1/', include('main.urls')),  # Include URLs from the main app with versioning
]