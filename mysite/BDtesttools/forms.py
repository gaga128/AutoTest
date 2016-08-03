from django import forms

class AddForm(forms.Form):
    appid=forms.in()
    uid=forms.int