from django import forms
from .models import *


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']


class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'time_lesson': DateInput()}
        fields = ['subject', 'title', 'description',
                  'time_lesson', 'is_finished']


class DashboardForm(forms.Form):
    text = forms.CharField(
        max_length=100, label='В ютубе вы можете найти любой контент! : ')
