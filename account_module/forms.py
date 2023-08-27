from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class Register_Form(forms.Form):
    firstName = forms.CharField(
        label='نام',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(25)
        ]
    )

    lastName = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(25)
        ]
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

    password = forms.CharField(
        label='پسورد',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    confirm_password = forms.CharField(
        label='تایید پسورد',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور با تکرار آن مطابقت ندارد')




class Login_Form(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

    password = forms.CharField(
        label="پسورد",
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

class ForgetPassForms(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs= {'placeholder' : 'لطفا ایمیل مورد نظر را وارد کنید'}
        ),
        validators = [
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )