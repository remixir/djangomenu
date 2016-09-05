from django.core.exceptions import ValidationError
from django.forms import ModelForm
from models import Tiles


class AdminMenuForm(ModelForm):
    class Meta:
        model = Tiles
        fields = ('__all__')

    def clean_parent(self):
        parent = self.cleaned_data['parent']
        if parent and parent.level >= 5:
            raise ValidationError('Recursion Depth Exceeded')
        return parent

