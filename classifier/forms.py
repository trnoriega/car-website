from django import forms
from .models import InputImage

class InputImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'btn btn-secondary my-2',
            }
            )
        )

    class Meta:
        model = InputImage
        fields = ('image',)
