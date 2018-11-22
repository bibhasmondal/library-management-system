from django import forms
from .models import *

class BookRequest(forms.ModelForm):
    remarks = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder': 'Remarks','max_length': 100}))
    class Meta:
        model = Request
        fields = ['remarks'] 

class New(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name','max_length': 100}))
    details = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Details','max_length': 100}))
    class Meta:
        model = New
        fields = ['name','details']

class BookAdd(forms.ModelForm):
    title = forms.CharField(label='Title',widget=forms.TextInput(attrs={'placeholder': 'Title','max_length': 100}))
    author = forms.CharField(label='Author',widget=forms.TextInput(attrs={'placeholder': 'Author','max_length': 100}))
    subject = forms.ModelChoiceField(label='Subject',widget=forms.Select(attrs={'max_length': 16}),queryset = Subject.objects.all(),initial=None)
    publisher = forms.CharField(label='Publisher',widget=forms.TextInput(attrs={'placeholder': 'Publisher','max_length': 100}))
    image = forms.ImageField(label='Image',widget=forms.FileInput(attrs={'type':'file','placeholder': 'Image','max_length': 100}))
    class Meta:
        model = Book
        fields = ['title','author','subject','publisher','image']