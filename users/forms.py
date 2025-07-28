from django import forms
from .models import CustomUser
import re

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        max_length=4,
        min_length=4,
        help_text="Enter a 4-digit numeric password."
    )

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'name', 'type', 'cooperative')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.fullmatch(r'\d{4}', password):
            raise forms.ValidationError("Password must be exactly 4 digits.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password) 
        if commit:
            user.save()
        return user
        
