from django.urls import path
from . import views

urlpatterns = [
    path("process_system/<int:pk>/", views.process_system, name="process_system"),
]
