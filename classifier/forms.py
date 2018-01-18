from django import forms
from .models import InputImage

class InputImageForm(forms.Form):
    image = forms.ImageField()
    prediction1 = forms.CharField(widget=forms.HiddenInput(), initial='', required=False)
    prediction2 = forms.CharField(widget=forms.HiddenInput(), initial='', required=False)
    prediction2 = forms.CharField(widget=forms.HiddenInput(), initial='', required=False)

    class Meta:
        model = InputImage
        fields = ('image',)
