from django.urls import path
from . import views

urlpatterns = [
    path('register/' , views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('forget-pass/' , views.ForgetPasswordView.as_view() , name='forget-pass-page'),
    path('reset-pass/<active_code>' , views.ResetPasswordView.as_view() , name='reset-password-page')

]