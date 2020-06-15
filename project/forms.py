from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Project
class ProductForm(forms.ModelForm):
    avatar = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'avatars'
        }
    )
    class Meta:
        model = Project
        fields = ('avatar', )