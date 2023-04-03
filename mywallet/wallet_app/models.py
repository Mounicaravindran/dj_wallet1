from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_gmail(value):
    if "@gmail.com" not in value:
        raise ValidationError("This email must be from Gmail domain only.")
    
def validate_phone_no(value):
    if not value.isdigit():
        raise ValidationError("Phone number can only contain digits")
    if len(value) != 10:
        raise ValidationError("Phone number must be 10 digits long")

class Wallet(models.Model):
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    email = models.EmailField(validators=[validate_gmail])
    phone_no =models.CharField(max_length=15,validators=[validate_phone_no])

