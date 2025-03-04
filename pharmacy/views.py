from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Medicine
from .forms import MedicineForm


class MedicineListView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})


class MedicineDetailView(View):
    def get(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        return render(request, 'pharmacy/medicine_detail.html', {'medicine': medicine})


class MedicineCreateView(View):
    def get(self, request):
        form = MedicineForm()
        return render(request, 'pharmacy/medicine_form.html', {'form': form})
    
    def post(self, request):
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
        return render(request, 'pharmacy/medicine_form.html', {'form': form})


class MedicineUpdateView(View):
    def get(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        form = MedicineForm(instance=medicine)
        return render(request, 'pharmacy/medicine_form.html', {'form': form})
    
    def post(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
        return render(request, 'pharmacy/medicine_form.html', {'form': form})


class MedicineDeleteView(View):
    def get(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        return render(request, 'pharmacy/medicine_confirm_delete.html', {'medicine': medicine})
    
    def post(self, request, pk):
        medicine = get_object_or_404(Medicine, pk=pk)
        medicine.delete()
        return redirect('medicine_list')
