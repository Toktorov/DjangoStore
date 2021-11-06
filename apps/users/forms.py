from apps.users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'profile_image', 'age',
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'profile_image': forms.FileInput(attrs={'class': "form-control"}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }