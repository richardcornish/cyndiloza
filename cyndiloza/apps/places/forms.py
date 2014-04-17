from django import forms
from localflavor.us.forms import USZipCodeField

from cyndiloza.apps.places.models import Place


class PlaceForm(forms.ModelForm):
    zipcode = USZipCodeField(label='ZIP code', required=False)

    class Meta:
        model = Place
