from django import forms
from captcha.fields import CaptchaField

class sinupForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255,widget=forms.PasswordInput)
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    tellnumber = forms.CharField(max_length=11,widget=forms.NumberInput)
    location = forms.CharField(max_length=255,required=False)
    birthday = forms.DateField()
    education = forms.CharField(max_length=255,required=False)
    langs = forms.CharField(max_length=255,required=False)
    cod_posti = forms.CharField(max_length=255,required=False)
    t_p = forms.CharField(max_length=255,required=False)
    email = forms.EmailField()
    captcha = CaptchaField()
    image= forms.ImageField(required=False)
    subject= forms.CharField(widget=forms.Textarea,required=False)
    