from django import forms
from todolist.models import TodoList
    
class TodolistForm(forms.ModelForm):
    class Meta:
        model = TodoList
        exclude = ('user', 'is_finished', )