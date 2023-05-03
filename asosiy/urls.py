from django.urls import path
from .views import *

urlpatterns = [
    path('mahsulot/<int:pk>/izohlar/', IzohlarAPIView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotAPIView.as_view()),
    path('mahsulotlar/', MahsulotlarAPIView.as_view()),
]