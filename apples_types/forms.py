from django.forms import ModelForm
from .models import Apples

class AddApple(ModelForm):
    class Meta:
        model=Apples
        fields="__all__"
