from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import api_us
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
    t_p = forms.IntegerField(required=False)
    email = forms.EmailField()
    captcha = CaptchaField()
    image= forms.ImageField(required=False)
    subject= forms.CharField(widget=forms.Textarea,required=False)
    
class api_us_form(ModelForm):
    
    class Meta:
        model = api_us
        fields = '__all__'