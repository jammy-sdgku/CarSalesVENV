from django import forms

class CarForm(forms.Form):
    id= forms.IntegerField()
    name= forms.CharField(max_length=100)
    year= forms.IntegerField()
    price= forms.FloatField(localize=True)