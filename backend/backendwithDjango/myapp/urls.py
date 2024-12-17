from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/hello/', views.hello_api, name='hello_api'),
    path('api/create_interaction/', views.create_interaction, name='create_interaction'),
]
