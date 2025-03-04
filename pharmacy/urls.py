# pharmacy/urls.py
from django.urls import path
from .views import (
    MedicineListView,
    MedicineDetailView,
    MedicineCreateView,
    MedicineUpdateView,
    MedicineDeleteView,
)

urlpatterns = [
    path('', MedicineListView.as_view(), name='medicine_list'),
    path('medicine/<int:pk>/', MedicineDetailView.as_view(), name='medicine_detail'),
    path('medicine/new/', MedicineCreateView.as_view(), name='medicine_create'),
    path('medicine/<int:pk>/edit/', MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), name='medicine_delete'),
]
