import pytest
from photography_app.models import Profile, User, Message

from django.test import Client

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User.objects.create(
        username='rarity',
        first_name='test',
        last_name='test',
        email='email@email.com',
    )

    return user


@pytest.fixture
def profile():
    user = User.objects.create(
        username='rarity',
        first_name='test',
        last_name='test',
        email='email@email.com',
    )
    profile = Profile.objects.create(
        user=user,
        description='test'
    )

    return profile



@pytest.fixture
def messages():
    message1= Message.objects.create(
        profile=profile,
        title='fake title',
        name='fake name',
        content='fake content',
        email='fake@email.com',
        date='10/10/2022'
    )

    message2 = Message.objects.create(
        profile=profile,
        title='fake title',
        name='fake name',
        content='fake content',
        email='fake@email.com',
        date='10/10/2022'
    )
    return message1, message2
