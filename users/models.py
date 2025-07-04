from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    is_google_account = models.BooleanField(default=False)
    profile_img = models.URLField(blank=True, null=True)
        
    def __str__(self):
        return self.username
