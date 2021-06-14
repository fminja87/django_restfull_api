from django.urls import path
from .views import StoryAPIView

urlpatterns = [
    path('generic/<int:id>/', StoryAPIView.as_view()),
]
