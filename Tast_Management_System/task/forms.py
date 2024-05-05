from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    TaskAssignDate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Task
        fields = "__all__"
