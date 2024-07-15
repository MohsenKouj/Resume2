from django import forms

class comment(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    title = forms.CharField(max_length=255)
    msg = forms.CharField(widget=forms.Textarea,required=False)
    
class contact(forms.Form):
    uname=forms.CharField(max_length=255)
    email=forms.EmailField()
    title=forms.CharField(max_length=255)
    mess=forms.CharField(widget=forms.Textarea,required=False)