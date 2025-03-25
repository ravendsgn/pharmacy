# pharmacy/urls.py
from django.urls import path
from .views import (
    MedicineListView,
    MedicineDetailView,
    MedicineCreateView,
    MedicineUpdateView,
    MedicineDeleteView,
    APICreateView,
    APIListView,
    APIDeleteView
)
from rest_framework import serializers

urlpatterns = [
    path('', MedicineListView.as_view(), name='medicine_list'),
    path('medicine/<int:pk>/', MedicineDetailView.as_view(), name='medicine_detail'),
    path('medicine/new/', MedicineCreateView.as_view(), name='medicine_create'),
    path('medicine/<int:pk>/edit/', MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), name='medicine_delete'),
    path('create/',APICreateView.as_view()),
    path('list/',APIListView.as_view())
]
