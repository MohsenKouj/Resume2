from django import forms

class comment(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)
    title = forms.CharField(max_length=255)
    msg = forms.CharField(widget=forms.Textarea)