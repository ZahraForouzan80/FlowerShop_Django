from django.shortcuts import render
from .models import Plant


def home(request):
    plants = Plant.objects.all()[:3]   # نمایش ۳ محصول آخر
    return render(request, "core/index.html", {"plants": plants})



def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'core/plants.html', {'plants': plants})