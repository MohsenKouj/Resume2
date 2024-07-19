from django import forms
from captcha.fields import CaptchaField

class captcha(forms.Form):
    captcha = CaptchaField()