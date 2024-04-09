from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ajoutez les champs supplémentaires ici si nécessaire
    date_of_birth = models.DateField(null=True, blank=True)