from django import forms

from WorldOfSpeed.mixins import ReadOnlyMixin
from cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }

class CarCreateForm(CarBaseForm):
    pass

class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    read_only_fields = ['type', 'model', 'year', 'image_url', 'price']

