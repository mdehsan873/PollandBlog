from django import forms
from .models import User
class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude=['user_name']