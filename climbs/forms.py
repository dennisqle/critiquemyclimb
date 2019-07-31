from django import forms
from .models import Climb

class ClimbForm(forms.ModelForm):
    class Meta:
        model = Climb
        fields = [
            'title',
            'video_url',
            'grade',
            'is_outdoor',
            'description',
        ]