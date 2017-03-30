from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Treasure
from .forms import TreasureForm
# Create your views here.

def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html', {'treasures': treasures, 'form': form})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasure(name=form.cleaned_data['name'],
                            value=form.cleaned_data['value'],
                            material=form.cleaned_data['material'],
                            location=form.cleaned_data['location'],
                            img_url=form.cleaned_data['img_url'])
        treasure.save()

    return HttpResponseRedirect('/')