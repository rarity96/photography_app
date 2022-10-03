from django.urls import reverse

import pytest
from photography_app.models import Profile, User, Message
# Create your tests here.

@pytest.mark.django_db
def test_create_user(client, user):
    assert User.objects.filter(username="rarity").exists()
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_create_user(client, profile):
    assert Profile.objects.filter(description="test").exists()


@pytest.mark.django_db
def test_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

