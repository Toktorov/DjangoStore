from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    profile_image = models.ImageField(upload_to = 'profile_image', blank = True, null = True)
    age = models.PositiveIntegerField(default=0, blank = True, null = True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-created', )