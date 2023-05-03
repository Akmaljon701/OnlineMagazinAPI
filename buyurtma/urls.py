from django.urls import path
from .views import *

urlpatterns = [
    path('tanlanganlar/', TanlanganlarAPIView.as_view()),
    path('tanlanganlar/<int:pk>/', TanlanganlarDetailAPIView.as_view()),

    path('savatlar/', SavatlarAPIView.as_view()),
    path('savatlar/<int:pk>/', SavatItemDetailAPIView.as_view()),

    path('<int:pk>/', BuyurtmaDetailView.as_view()),
    path('', BuyurtmalarAPIView.as_view()),

]