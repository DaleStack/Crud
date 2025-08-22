from django import forms
from .models import NoteModel


class NoteModelForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'content']