from django import forms

class TreasureForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    value = forms.DecimalField(label='Value', max_digits=10, decimal_places=2)
    material = forms.CharField(label='Material', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
    img_url = forms.CharField(label='Image URL', max_length=200)