from django import forms
from django.contrib.localflavor.us.forms import USZipCodeField

from cyndiloza.places.models import Place


class PlaceForm(forms.ModelForm):
    zipcode = USZipCodeField(label='ZIP code', required=False)

    class Meta:
        model = Place
