from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile' , verbose_name='UserImage' , null=True , blank=True)
    email_active_code = models.CharField(max_length=100 , verbose_name='active_code' )
    about_user = models.TextField(verbose_name='about_user' , null=True , blank=True)
    address = models.TextField(verbose_name='address' , null=True , blank=True)


    class Meta:
        ordering =['first_name']
        permissions = [("user_yes" , "useryes")]
        verbose_name='user'
        verbose_name_plural = 'users'


    def save(self, *args, **kwargs):
        if self.first_name == 'aliasghar':
            return print("Dont Allow Save!!!")
        else:
            super().save(*args , **kwargs)


    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email