from django.shortcuts import render

# Create your views here.

class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure("Gold Nugget", 500.00, "gold", "Curly's Creek, NM"),
    Treasure("Fool's Glod", 0, "pyrite", "Fool's Falls, CO"),
    Treasure("Coffee Can", 500.00, "tin", "ACME, CA"),
]

def index(request):
    name = 'Gold Nugget'
    value = 1000.00
    context = {'treasure_name': name,
               'treasure_val': value}

    return render(request, 'index.html', context)
