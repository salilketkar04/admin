from django import forms
#import model class from models.py
#from app_name.models import model_name
from countries.models import Countries

class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = "__all__"
