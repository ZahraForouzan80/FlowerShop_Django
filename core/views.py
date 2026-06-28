from .models import Plant
from django.shortcuts import render, redirect
from .forms import RegisterForm


def home(request):
    plants = list(Plant.objects.all())

    plant_groups = []

    for i in range(0, len(plants), 3):
        plant_groups.append(plants[i:i+3])

    return render(request, "core/index.html", {
        "plant_groups": plant_groups
    })

def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'core/plants.html', {'plants': plants})

def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "core/register.html", {"form": form})

def login(request):
    return render(request, "core/login.html")
    