from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from ckeditor.fields import RichTextField

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=255)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)


class Gallery(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = RichTextField(blank=True, null=True)
    teaser = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Photos(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to="images/post/")


class Availability(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    booked = models.BooleanField(default=False, null=True)
    reserved = models.BooleanField(default=False, null=True)
    short_message = models.CharField(max_length=128, null=True)


class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    name = models.CharField(max_length=64, null=True)
    content = models.TextField()
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
