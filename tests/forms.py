from django import forms
from .models import FileModel


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileModel
