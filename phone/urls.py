from django.urls import path
from .views import Phones, PhoneDetails

urlpatterns = [
    path('', Phones.as_view()),
    path('details/<int:id>/', PhoneDetails.as_view()),
]
