from django import forms
from .models import Product


class ProductUpload(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Title', 'Description', 'Image', 'ModelFile']

        # widgets = {
        #     'Title': forms.TextInput(),
        #     'Description': forms.TextInput(),
        #     'Image': forms.FileInput()
        # }
