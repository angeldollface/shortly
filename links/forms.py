from django import forms

class LinkForm(forms.Form):
    url = forms.CharField(label='Link URL', max_length=300)
    name = forms.CharField(label='Link Name', max_length=200)