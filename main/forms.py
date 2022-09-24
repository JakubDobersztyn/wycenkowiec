from django.forms import ModelForm
from main.models import Pricing, Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'unit', 'unit_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update({'class': 'form-control'})