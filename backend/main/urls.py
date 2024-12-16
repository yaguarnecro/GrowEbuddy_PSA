from django.urls import path
from .views import VpetListView, ChallengeListView  # Import your views

urlpatterns = [
    path('vpets/', VpetListView.as_view(), name='vpet-list'),  # Example route for Vpets
    # path('notes/', NoteListView.as_view(), name='note-list'),  # Commented out or removed
    path('challenges/', ChallengeListView.as_view(), name='challenge-list'),  # Example route for Challenges
]