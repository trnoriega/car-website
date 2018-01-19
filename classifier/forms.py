from django import forms
from .models import InputImage

class InputImageForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = InputImage
        fields = ('image',)
