from django import forms
from todolist.models import TodoList
    
class TodolistForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title','description']

    
    title_attrs = {
        'type' : 'text',
        'placeholder' : 'Title',
        'class' : 'form-control'
    }

    description_attrs = {
        'type' : 'text',
        'placeholder' : 'Description',
        'class' : 'form-control'
    }

    title = forms.CharField(label="Title",required=True,
    max_length=50,widget=forms.TextInput(attrs=title_attrs))

    description = forms.CharField(widget=forms.Textarea(attrs=description_attrs))