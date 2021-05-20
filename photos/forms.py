from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Photo


class PhotoModelForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        labels = {
            'image': None #_('Upload an image here'),
        }
