from django.urls import reverse
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
def test_user_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    url = reverse('register')
    response = client.post(url, user_data)
    assert user_model.objects.count() == 1
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_invalid_signup(client, user_invalid_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    url = reverse('register')
    response = client.post(url, user_invalid_data)
    assert response.status_code == 400
    assert user_model.objects.count() == 0


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    url = reverse('login')
    response = client.post(url, user_data)
    assert response.status_code == 200
    assert response.data['access'] is not None

