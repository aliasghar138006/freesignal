from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.http import  HttpRequest
from utils.email_services import send_email

from .forms import Register_Form , Login_Form , ForgetPassForms
from .models import User

# Create your views here.


# def register(request):
#     return render(request , 'register.html' , {})

class RegisterView(View):
    def get(self, request):
        context = {
            'register_form' : Register_Form()
        }
        return  render(request , 'register.html' , context)


    def post(self, request):
        register_form = Register_Form(request.POST)
        if register_form.is_valid():
            user_firstName = register_form.cleaned_data.get('firstName')
            user_lastName = register_form.cleaned_data.get('lastName')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')

            user : bool  = User.objects.filter(email__iexact=user_email).exists()

            if user:
                register_form.add_error('email' , 'this email exact')
            else:
                new_user = User(
                    first_name=user_firstName,
                    last_name=user_lastName,
                    email=user_email,
                    username=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login_page'))

        context = {
            'register_form' : register_form
        }

        return render(request , 'register.html' , context)




# def login_page(request):
#     return render(request , 'login.html' , {})


class LoginView(View):
    def get(self , request):
        login_form = Login_Form()
        context = {
            "login_form":login_form
        }
        return render(request , 'login.html' , context)

    def post(self, request):
        login_form = Login_Form(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user : User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email' , 'حساب فعال نشده است')
                else:
                    password_verify = user.check_password(user_pass)
                    if password_verify:
                        login(request , user)
                        return redirect(reverse('home'))
                    else:
                        login_form.add_error('password' , 'password Not Correct!!')
            else:
                login_form.add_error('email' , 'Not Found User!!')

        context = {
                "login_form":login_form
        }

        return render(request,'login.html' , context)


class ForgetPasswordView(View):
    def get(self , request):
        forgetform = ForgetPassForms()
        context = {
            'forgetform' : forgetform
        }
        return render(request , 'forgetpasspage.html' , context)
    def post(self , request:HttpRequest):
        forgetform = ForgetPassForms(request.POST)
        if forgetform.is_valid():
            user_email = forgetform.cleaned_data.get('email')
            user : User = User.objects.filter(email__iexact=user_email).first()
            if user:

                send_email('بازیابی کلمه عبور' , user.email , {'user' : user} , 'emails/emailpass.html'  )
                context={
                    'message' : 'جهت تغییر رمز عبور به ایمبل خود مراجعه کنید'
                }
                return render(request , 'forgetpasspage.html' , context)
            else:
                forgetform.add_error('email' , 'email Not Found!!')

        context = {
            'forgetform' : forgetform
        }

        return render(request , 'forgetpasspage.html' , context)


class ResetPasswordView(View):
    def get(self , request , active_code):
        print(active_code)
        return render(request , 'resetpasspage.html' , {})
    def post(self , request):
        pass

