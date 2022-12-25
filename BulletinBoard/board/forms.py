from django import forms
from .models import Bulletin
from tinymce.widgets import TinyMCE


class BulletinForm(forms.ModelForm):
    #body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Bulletin
        fields = [
            'owner',
            'header',
            'body',
            'category',
        ]
        widgets = {
            'body': TinyMCE(attrs={
                'cols': 80,
                'rows': 30,
                'class': 'form-control'
            })
        }
