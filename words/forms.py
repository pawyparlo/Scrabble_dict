from django import forms

class LettersForm(forms.Form):
    letters = forms.CharField(max_length=7)