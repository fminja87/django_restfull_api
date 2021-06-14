from django.urls import path, include
from .views import article_list, article_details, ArticleAPIView, ArticleDetail, GenericAPIView

urlpatterns = [
    path('', article_list),
    path('class/', ArticleAPIView.as_view()),
    path('details/<int:pk>/', article_details),
    path('class/details/<int:id>/', ArticleDetail.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]
