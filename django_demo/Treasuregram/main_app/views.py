from django.shortcuts import render

# Create your views here.

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure("Gold Nugget", 500.00, "gold", "Curly's Creek, NM", 'http://courseware.codeschool.com/try_django/images/treasuregram-gold-nugget.png'),
    Treasure("Fool's Glod", 0, "pyrite", "Fool's Falls, CO", 'http://courseware.codeschool.com/try_django/images/treasuregram-fools-gold.png'),
    Treasure("Coffee Can", 500.00, "tin", "ACME, CA", 'http://courseware.codeschool.com/try_django/images/treasuregram-coffee-can.png'),
]

def index(request):
    return render(request, 'index.html', {'treasures': treasures})
