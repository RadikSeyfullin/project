from django import forms
from .models import TodoList

class AddForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('title',)
