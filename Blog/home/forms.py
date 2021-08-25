from django import forms
from django.contrib.auth.forms import UserCreationForm
from simplemathcaptcha.fields import MathCaptchaField
from simplemathcaptcha.widgets import MathCaptchaWidget
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from home.models import blog
import re


class SignupForm(UserCreationForm):
    
    captcha = MathCaptchaField(widget=MathCaptchaWidget(question_tmpl=(' %(num1)i %(operator)s %(num2)i = ')))
    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if len(r):
            raise  ValidationError("Username already exists !")
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        regex = "^(?=.*[a-zA-Z])(?=.*[0-9])[A-Za-z0-9]+$"
        p = re.compile(regex)
        if re.search(p, password1):
            return password1
        raise ValidationError('password should be alpanumric!')


class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title','description','image','mode']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.Textarea(attrs={'class':'form-control'}),
        'mode':forms.RadioSelect(),
        'image':forms.ClearableFileInput(attrs={'class':'form-control'})}