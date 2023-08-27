from django.db import models

# Create your models here.

class contactModel(models.Model):
    firstName = models.CharField(max_length=100 , verbose_name="firstName")
    lastName = models.CharField(max_length=100 , verbose_name="lastName")
    comment = models.TextField(verbose_name="Comment")

    class Meta:
        permissions=[("contact_yes" , "contactyes")]
