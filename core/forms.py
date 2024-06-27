from django.forms import ModelForm
from core.models import House, Image
from django import forms



class HouseForm(forms.ModelForm):
    image = forms.ImageField(label='Upload Image', required=False)
    
    class Meta:
        model = House
        fields = ["name", "postcode", "description", "status", "image", "link"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['postcode'].required = False

