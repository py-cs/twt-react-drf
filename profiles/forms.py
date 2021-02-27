from .models import Profile
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ['location', 'bio']
