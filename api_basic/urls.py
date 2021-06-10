from django.urls import path, include
from .views import article_list, article_details

urlpatterns = [
    path('article/', article_list),
    path('article/details/<int:pk>/', article_details),
]
