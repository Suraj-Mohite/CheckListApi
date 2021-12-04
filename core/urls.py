from django.urls import path
from core.views import (
    ChecklistsAPIView,
    ChecklistAPIView,
    ChecklistItemAPIView,
    ChecklistItemCreateAPIView
    )

urlpatterns = [
path('api/checklist/',ChecklistsAPIView.as_view()),
path('api/checklist/<int:pk>/',ChecklistAPIView.as_view()),
path('api/checklistitem/create/',ChecklistItemCreateAPIView.as_view()),
path('api/checklistitem/<int:pk>/',ChecklistItemAPIView.as_view()),
]


