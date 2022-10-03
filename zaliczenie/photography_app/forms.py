from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Gallery, Contact, Photos

User = get_user_model()


class AddContactInfo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = '__all__'
