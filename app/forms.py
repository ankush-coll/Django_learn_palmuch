from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        email = forms.EmailField(required=True)
        fields = ['username', 'email', 'password1', 'password2']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        # Remove help text for password fields
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None

